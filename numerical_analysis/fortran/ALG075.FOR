C***********************************************************************
C                                                                      *
C                   CONJUGATE GRADIENT ALGORITHM 7.5                   *          
C                                                                      *
C***********************************************************************
C
C
C
C     TO SOLVE AX = B GIVEN THE PRECONDITIONING MATRIX C INVERSE AND AN 
C     INITIAL APPROXIMATION X(0):
C
C     INPUT:   THE NUMBER OF EQUATIONS AND UNKNOWNS n; THE ENTRIES
C              A(I,J), 1<=I, J<=n, OF THE MATRIX A; THE ENTRIES B(I),
C              1<=I<=n, OF THE INHOMOGENEOUS TERM B; THE ENTRIES
C              C(I,J), 1<=I, J<=n OF THE PRECONDITIONING MATRIX C
C              INVERSE,THE ENTRIES XO(I), 1<=I<=n, OF X(0); TOLERANCE
c              TOL; MAXIMUM NUMBER OF ITERATIONS N; 
C
C     OUTPUT:  THE APPROXIMATE SOLUTION X(1),...,X(n) OR A MESSAGE
C              THAT THE NUMBER OF ITERATIONS WAS EXCEEDED.
C
C     INITIALIZATION
      DIMENSION A(10,11),CI(10,10),CT(10,10),X1(10),R(10),V(10)
      DIMENSION W(10),U(10),Z(10)
C     USE NN FOR CAPITAL N
C     B(I) = A(I,n+1) FOR 1<=I<=n
C     USE X1 FOR XO
      CHARACTER NAME*30,NAME1*30,AA*1
      INTEGER INP,OUP,FLAG
      LOGICAL OK
      OPEN(UNIT=5,FILE='CON',ACCESS='SEQUENTIAL')
      OPEN(UNIT=6,FILE='CON',ACCESS='SEQUENTIAL')
      WRITE(6,*) 'This is the Conjugate Gradient Method'
      WRITE(6,*) 'for Linear Systems.'
      WRITE(6,*) 'The array will be input from a text file in the'
      WRITE(6,*) ' order: A(1,1), A(1,2), ..., A(1,n+1), A(2,1),'
      WRITE(6,*) ' A(2,2), ..., A(2,n+1)..., A(n,1), A(n,2),'
      WRITE(6,*) ' ..., A(n,n+1) '
      WRITE(6,*) 'Place as many entries as desired on each line,'
      WRITE(6,*) ' but separate entries with at least one blank.'
      WRITE(6,*) 'The preconditioner, C inverse, should '
      WRITE(6,*) 'follow in the same way.'
      WRITE(6,*) 'The initial approximation should also follow in the'
      WRITE(6,*) 'same format.'
      OK = .FALSE.
      WRITE(6,*) 'Has the input file been created?'
      WRITE(6,*) 'Enter Y or N - letter within quotes '
      WRITE(6,*) ' '
      READ(5,*)  AA
      IF (( AA .EQ. 'Y' ) .OR.( AA .EQ. 'y' )) THEN
         WRITE(6,*) 'Input the file name in the form - '
         WRITE(6,*) 'drive:name.ext  contained in quotes'
         WRITE(6,*) 'as example:   ''A:DATA.DTA'' '
         WRITE(6,*) ' '
         READ(5,*)  NAME
         INP = 4
         OPEN(UNIT=INP,FILE=NAME,ACCESS='SEQUENTIAL')
         OK = .FALSE.
19       IF (OK) GOTO 111
         WRITE(6,*) 'Input the number of equations - an integer '
         WRITE(6,*)
         READ(5,*) N
         IF (N .GT. 0) THEN
            M = N+1
            READ(INP,*) ((A(I,J), J=1,M),I=1,N)
            READ(INP,*) ((CI(I,J), J=1,N),I=1,N)
            READ(INP,*) (X1(I),I=1,N)
          OK = .TRUE.
            CLOSE(UNIT=INP)
         ELSE
            WRITE(6,*) 'The number must be a positive integer'
         ENDIF
         GOTO 19
111      OK = .FALSE.
12       IF (OK) GOTO 13
         WRITE(6,*) 'Input the tolerance.'
         WRITE(6,*) ' '
         READ(5,*) TOL
         IF (TOL .GT. 0.0) THEN
            OK = .TRUE.
         ELSE
            WRITE(6,*) 'Tolerance must be positive.'
         ENDIF
         GOTO 12
13       OK = .FALSE.
14       IF (OK) GOTO 15
         WRITE(6,*) 'Input maximum number of iterations.'
         WRITE(6,*)
         READ(5,*) NN
         IF (NN .GT. 0) THEN
            OK = .TRUE.
         ELSE
            WRITE(6,*) 'Number must be a positive integer.'
         ENDIF
         GOTO 14
      ELSE
         WRITE(6,*) 'The program will end so the input file can '
         WRITE(6,*) 'be created. '
         OK = .FALSE.
      ENDIF
15    IF(.NOT. OK) GOTO 400
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
      WRITE(OUP,*) 'CONJUGATE GRADIENT METHOD FOR LINEAR SYSTEMS'
      WRITE(OUP,3)
      WRITE(OUP,4) ((A(I,J),J=1,M),I=1,N)
      WRITE(OUP,5)
      WRITE(OUP,4) ( X1(I) ,I=1,N)
C     STEP 1
      DO 22 I=1,N
         DO 22 J=1,N
22          CT(I,J) = CI(J,I)
      DO 17 I=1,N
         R(I) =  A(I,N+1)       
         DO 17 J=1,N
17          R(I) = R(I) - A(I,J)*X1(J)
      DO 18 I=1,N
         W(I) = 0.0
         DO 18 J=1,N
18          W(I) = W(I) + CI(I,J)*R(J)
      DO 23 I=1,N
         V(I) = 0.0
         DO 23 J=1,N
23          V(I) = V(I) + CT(I,J)*W(J)
      ALPHA = 0.0
      DO 21 I=1,N
21       ALPHA = ALPHA + W(I)*W(I)
C     STEP 2
      K=1
      OK = .FALSE.
C     STEP 3
100   IF ((K.GT.NN) .OR. OK) GOTO 200
           ERR=0.0
C          ERR WILL BE USED TO TEST ACCURACY, IT MEASURES THE
C          2-NORM
C          STEP 4
           DO 10 I=1,N
10            ERR = ERR + V(I)*V(I)
           IF(SQRT(ERR) .LT. TOL) THEN
                WRITE(OUP,7) K,TOL
                GOTO 400
           ENDIF
C          STEP 5
           DO 20 I=1,N
              U(I) = 0.0
              DO 20 J=1,N
20               U(I) = U(I) + A(I,J)*V(J)
           S=0
           DO 30 I=1,N
30            S = S + V(I)*U(I)
           T = ALPHA/S
           DO 40 I = 1,N
              X1(I) = X1(I) + T*V(I)
40            R(I) = R(I) - T*U(I)
           WRITE(OUP,6) K,(X1(I),I=1,N)
           WRITE(OUP,11) (R(I),I=1,N)
           DO 50 I = 1,N
              W(I) = 0.0
              DO 50 J = 1,N
50               W(I) = W(I) + CI(I,J)*R(J)
           BETA = 0
           DO 60 I = 1,N
60            BETA = BETA + W(I)*W(I)
C     STEP 6
           IF(SQRT(BETA) .LE. TOL) THEN
              ERR = 0.0
              DO 70 I = 1,N
70               ERR = ERR + R(I)*R(I)
              IF(SQRT(ERR) .LT. TOL) THEN
                WRITE(OUP,7) K, TOL
                GOTO 400
              ENDIF
           ENDIF
C          STEP 7
           S = BETA/ALPHA
           DO 80 I = 1,N
              Z(I) = 0
              DO 80 J  = 1,N
80               Z(I) = Z(I) + CT(I,J)*W(J)
           DO 90 I = 1,N
90            V(I) = Z(I) + S*V(I)
           ALPHA = BETA
           K=K+1
      GOTO 100
C     STEP 8
C     PROCEDURE COMPLETED SUCCESSFULLY
200   CONTINUE
      WRITE(OUP,8)
400   CLOSE(UNIT=5)
      CLOSE(UNIT=OUP)
      IF(OUP.NE.6) CLOSE(UNIT=6)
      STOP
3     FORMAT(1X,'ORIGINAL SYSTEM:')
4     FORMAT((1X,6(1X,E15.8)))
5     FORMAT(1X,'INITIAL APPROXIMATION:')
6     FORMAT(1X,'ITERATION NUMBER ',I3,' GIVES ',
     *'APPROX.',5(1X,E15.8))
7     FORMAT(1X,'CONVERGENCE ON INTERATION NUMBER ',I4,/,
     *' TOLERANCE = ',E15.8)
8     FORMAT(1X,'Maximum Number of Iterations Exceeded.')
11    FORMAT(1X,'RESIDUAL IS ',5(1X,E15.8))
      END
