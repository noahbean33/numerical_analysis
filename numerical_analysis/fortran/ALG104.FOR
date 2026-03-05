C***********************************************************************
C                                                                      *
C             CONTINUATION METHOD FOR SYSTEMS ALGORITHM 10.4           *
C                                                                      *
C***********************************************************************
C
C
C
C     TO APPROXIMATE THE SOLUTION OF THE NONLINEAR SYSTEM F(X)=0 GIVEN
C     AN INITIAL APPROXIMATION X:
C
C     INPUT:   NUMBER n OF EQUATIONS AND UNKNOWNS; INITIAL APPROXIMATION
C              X=(X(1),...,X(n)); NUMBER OF RUNGE-KUTTA ITERATIONS N1
C
C     OUTPUT:  APPROXIMATE SOLUTION X=(X(1),...,X(n))
C
C     INITIALIZATION
      DIMENSION AA(3,4),Y(3),X(3),RK1(4,3),B(3),X1(3),RMM(4)
C     USE AA FOR J;  
      CHARACTER NAME1*30,AAA*1
      INTEGER OUP,FLAG
      LOGICAL OK
      OPEN(UNIT=5,FILE='CON',ACCESS='SEQUENTIAL')
      OPEN(UNIT=6,FILE='CON',ACCESS='SEQUENTIAL')
      WRITE(6,*) 'This is the Continuation Method for Nonlinear '
      WRITE(6,*) 'Systems.  Has the function F been defined and has'
      WRITE(6,*) 'the Jacobian of partial derivatives been defined'
      WRITE(6,*) 'at lines 90 and 104 respectively.'
      WRITE(6,*) 'Enter Y or N '
      WRITE(6,*) ' '
      READ(5,*)  AAA
      IF(( AAA .EQ. 'Y' ) .OR. ( AAA .EQ. 'y' )) THEN
         OK = .FALSE.
101      IF (OK) GOTO 11
            WRITE(6,*) 'Input the number n of equations.'
            WRITE(6,*) ' '
            READ(5,*) N
            IF (N.GE.2) THEN
               OK = .TRUE.
            ELSE
               WRITE(6,*) 'N must be greater than 1.'
            ENDIF
         GOTO 101
11       OK = .FALSE.
12       IF (OK) GOTO 13
            WRITE(6,*) 'Input the number of RK4 iterations.'
            WRITE(6,*) ' '
            READ(5,*) N1
            IF ( N1 .LE. 0 ) THEN
              WRITE(6,*) 'Must be positive integer '
            ELSE
              OK = .TRUE.
            ENDIF
         GOTO 12
13       DO 16 I=1,N
            WRITE(6,*) 'Input initial approximation X(',I,')'
            WRITE(6,*) ' '
            READ(5,*) X1(I)
16       CONTINUE
      ELSE
         WRITE(6,*) 'The program will end so that the functions'
         WRITE(6,*) 'F(X) and J(X) can be created '
         OK = .FALSE.
      ENDIF
      IF(.NOT.OK) GOTO 400
      WRITE(6,*) 'Select output destination: '
      WRITE(6,*) '1. Screen '
      WRITE(6,*) '2. Text file '
      WRITE(6,*) 'Enter 1 or 2 '
      WRITE(6,*) ' '
      READ(5,*) FLAG
      IF ( FLAG .EQ. 2 ) THEN
         WRITE(6,*) 'Input the file name in the form - '
         WRITE(6,*) 'drive:name.ext'
         WRITE(6,*) 'with the name contained within quotes'
         WRITE(6,*) 'as example:   ''A:OUTPUT.DTA'' '
         WRITE(6,*) ' '
         READ(5,*) NAME1
         OUP = 3
         OPEN(UNIT=OUP,FILE=NAME1,STATUS='NEW')
      ELSE
         OUP = 6
      ENDIF
      WRITE(OUP,*) 'CONTINUATION METHOD FOR NONLINEAR SYSTEMS'
      PI = 4*ATAN(1.)
C     STEP 1
      K=1
      H=1.0/N1
C     COMPUTE -H*F(X)- USE X1 IN PLACE OF X IN THE FUNCTION
      B(1)=-H*(3*X1(1)-COS(X1(2)*X1(3))-.5)
      B(2)=-H*(X1(1)**2-81*(X1(2)+.1)**2+SIN(X1(3))+1.06)
      B(3)=-H*(EXP(-X1(1)*X1(2))+20*X1(3)+(10*PI-3)/3)
      RMM(1) = 0.5
      RMM(2) = 0.5
      RMM(3) = 1.0
      RMM(4) = 0.0
C     STEP 2
100   IF (K.GT.N1) GOTO 400
C          STEPS 3 - 6
           DO 14 I = 1, N
14         X(I) = X1(I)
           KK = 1
21         IF(KK.GT.4) GOTO 22
C          COMPUTE JACOBIAN
           AA(1,1)=3.0
           AA(1,2)=X(3)*SIN(X(2)*X(3))
           AA(1,3)=X(2)*SIN(X(2)*X(3))
           AA(2,1)=2*X(1)
           AA(2,2)=-162*(X(2)+.1)
           AA(2,3)=COS(X(3))
           AA(3,1)=-X(2)*EXP(-X(1)*X(2))
           AA(3,2)=-X(1)*EXP(-X(1)*X(2))
           AA(3,3)=20
           DO 26 I=1,N
26         AA(I,N+1)=B(I)
C          SOLVES THE N X N LINEAR SYSTEM J(X) Y = -F(X)
           CALL LIN(N,N+1,AA,Y)
           DO 20 I = 1,N
              RK1(KK,I) = Y(I)
20         X(I) = X1(I)+RMM(KK)*RK1(KK,I)
           KK=KK+1
           GOTO 21
22         DO 23 I=1,N
C       STEP 7
23         X1(I)=X1(I)+(RK1(1,I)+2*RK1(2,I)+2*RK1(3,I)+RK1(4,I))/6
           WRITE(OUP,3) K,(X1(I),I=1,N)
           K = K + 1
           GOTO 100
400   CLOSE(UNIT=5)
      CLOSE(UNIT=OUP)
      IF(OUP.NE.6) CLOSE(UNIT=6)
      STOP
3     FORMAT(1X,'ITER.=',1X,I2,1X,'APPROX. SOL. IS',1X,3(1X,E15.8))
      END
C
           SUBROUTINE LIN(N,M,A,X)
C          LIN SOLVES THE LINEAR SYSTEM: J(X) Y = -F(X) USING PARTIAL
C          PIVOTING
           DIMENSION A(N,M),X(N)
           ZERO = 1.0E-20
           K=N-1
           DO 10 I=1,K
                Y=ABS(A(I,I))
                IR=I
                IA=I+1
                DO 20 J=IA,N
                     IF(ABS(A(J,I)).GT.Y) THEN
                          IR=J
                          Y=ABS(A(J,I))
                     END IF
20              CONTINUE
                IF(Y.LE.ZERO) THEN
                     WRITE(6,1)
                     STOP
                END IF
                IF(IR.NE.I) THEN
                     DO 30 J=I,M
                          C=A(I,J)
                          A(I,J)=A(IR,J)
30                   A(IR,J)=C
                END IF
                DO 40 J=IA,N
                     C=A(J,I)/A(I,I)
                     IF(ABS(C).LE.ZERO) C=0
                     DO 40 L=I,M
40              A(J,L)=A(J,L)-C*A(I,L)
10         CONTINUE
           IF(ABS(A(N,N)).LT.1.0E-20) THEN
                WRITE(6,1)
                STOP
           END IF
      X(N)=A(N,M)/A(N,N)
      DO 50 I=1,K
           J=N-I
           JA=J+1
           C=A(J,M)
           DO 60 L=JA,N
60        C=C-A(J,L)*X(L)
50    X(J) = C/A(J,J)
      RETURN
1     FORMAT(1X,'LINEAR SYSTEM HAS NO SOLUTION')
      END
