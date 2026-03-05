C***********************************************************************
C                                                                      *
C                  ITERATIVE REFINEMENT ALGORITHM 7.4                  *
C                                                                      *
C***********************************************************************
C
C
C     TO APPROXIMATE THE SOLUTION TO THE LINEAR SYSTEM AX=B WHEN A IS
C     SUSPECTED TO BE ILL-CONDITIONED:
C
C     INPUT:   THE NUMBER OF EQUATIONS AND UNKNOWNS n; THE ENTRIES
C              A(I,J), 1<=J, J<=n, OF THE MATRIX A; THE ENTRIES B(I),
C              1<=I<=n, OF THE INHOMOGENEOUS TERM B; THE MAXIMUM NUMBER
C              OF ITERATIONS N; TOLERANCE TOL.
C
C     OUTPUT:  THE APPROXIMATION XX(1),...,XX(n) OR A MESSAGE THAT THE
C              NUMBER OF ITERATIONS WAS EXCEEDED.
C
C     INITIALIZATION
      IMPLICIT REAL*8(A-H,O-Z)
      DIMENSION R(10),B(10,11),XX(10)
      DIMENSION A(10,11),X(10),NROW(10)
C     NN IS A BOUND FOR THE NUMBER OF ITERATIONS
      CHARACTER NAME*30,NAME1*30,AA*1
      INTEGER INP,OUP,FLAG,RND,D,N,M,I,J,NN,KKK,KK,L,JJ,LL,I1,J1
      LOGICAL OK
      OPEN(UNIT=5,FILE='CON',ACCESS='SEQUENTIAL')
      OPEN(UNIT=6,FILE='CON',ACCESS='SEQUENTIAL')
      WRITE(6,*) 'This is the Iterative Refinement Method.'
      WRITE(6,*) 'The array will be input from a text file in the'
      WRITE(6,*) ' order: A(1,1), A(1,2), ..., A(1,n+1), A(2,1),'
      WRITE(6,*) ' A(2,2), ..., A(2,n+1)..., A(n,1), A(n,2),'
      WRITE(6,*) ' ..., A(n,n+1) '
      WRITE(6,*) 'Place as many entries as desired on each line,'
      WRITE(6,*) ' but separate entries with at least one blank.'
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
119      IF (OK) GOTO 111
         WRITE(6,*) 'Input the number of equations - an integer '
         WRITE(6,*)
         READ(5,*) N
         IF (N .GT. 0) THEN
            M = N+1
            READ(INP,*) ((A(I,J), J=1,M),I=1,N)
          OK = .TRUE.
            CLOSE(UNIT=INP)
         ELSE
            WRITE(6,*) 'The number must be a positive integer'
         ENDIF
         GOTO 119
111      OK = .FALSE.
114      IF (OK) GOTO 115
         WRITE(6,*) 'Input maximum number of iterations.'
         WRITE(6,*)
         READ(5,*) NN
         IF (NN .GT. 0) THEN
            OK = .TRUE.
         ELSE
            WRITE(6,*) 'Number must be a positive integer.'
         ENDIF
         GOTO 114
      ELSE
         WRITE(6,*) 'The program will end so the input file can '
         WRITE(6,*) 'be created. '
         OK = .FALSE.
      ENDIF
      IF(.NOT.OK) GO TO 400
115   WRITE(6,*) 'Choice of Rounding or Chopping'
      WRITE(6,*) '1. Rounding'
      WRITE(6,*) '2. Chopping'
      WRITE(6,*) 'Enter 1 or 2'
      READ(5,*) RND
      OK = .FALSE.
116   IF(OK) GOTO 117
      WRITE(6,*) 'Input number of digits D <= 8 of rounding'
      READ(5,*) D
      IF(D.GT.0) THEN
         OK = .TRUE.
      ELSE
         WRITE(6,*) 'D must be a positive integer.'
      ENDIF
      GOTO 116
117   OK = .FALSE.
118   IF(OK) GOTO 121
      WRITE(6,*) 'Input tolerance, which is usually 10**(-D)'
      READ(5,*) TOL
      IF(TOL.GT.0.0) THEN
         OK = .TRUE.
      ELSE
         WRITE(6,*) 'Tolerance must be a positive number.'
      ENDIF
      GOTO 118
121   WRITE(6,*) 'Select output destination: '
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
      WRITE(OUP,*) 'ITERATIVE REFINEMENT METHOD'
      WRITE(OUP,4)
      WRITE(OUP,5) ((A(I,J),J=1,M),I=1,N)
      DO 10 I=1,N
           NROW(I)=I
           DO 10 J=1,M
           C = CHIP(RND,D,A(I,J))
           A(I,J) = C
10         B(I,J) = C
      IF(RND.EQ.1) THEN
         WRITE(OUP,211) D
211      FORMAT(1X,'ROUNDING TO ',I3,' DIGITS')
      ELSE
         WRITE(OUP,212) D
212      FORMAT(1X,'CHOPPING TO ',I3,' DIGITS')
      ENDIF
      WRITE(OUP,*) 'MODIFIED SYSTEM'
      WRITE(OUP,5) ((A(I,J),J=1,M),I=1,N)
C     NROW AND B HAVE BEEN INITIALIZED
C     GAUSS ELIMINATION WILL BEGIN
C     STEP 0
      KKK=N-1
      DO 21 I=1,KKK
           KK=I
200        IF (DABS(A(KK,I)).GE.1.0E-20 .OR. KK.GT.N) GOTO 300
               KK=KK+1
           GOTO 200
300        IF(KK.GT.N) THEN
                WRITE(OUP,6)
                GOTO 400
           END IF
           IF(KK.NE.I) THEN
C               ROW INTERCHANGE NECESSARY
                IS=NROW(I)
                NROW(I)=NROW(KK)
                NROW(KK)=IS
                DO 40 J=1,M
                     C=A(I,J)
                     A(I,J)=A(KK,J)
40              A(KK,J)=C
           END IF
           KK=I+1
           DO 20 J=KK,N
           A(J,I)=CHIP(RND,D,A(J,I)/A(I,I))
           DO 20 L=KK,M
           CC=CHIP(RND,D,A(J,I)*A(I,L))
20    A(J,L)=CHIP(RND,D,A(J,L)-CC)
21    CONTINUE
      IF(DABS(A(N,N)).LT.1.0E-20) THEN
           WRITE(OUP,6)
           GOTO 400
      END IF
      X(N)=CHIP(RND,D,A(N,M)/A(N,N))
      DO 50 I=1,KKK
           J=N-I
           JJ=J+1
           S=0
           DO 60 L=JJ,N
           CC=CHIP(RND,D,A(J,L)*X(L))
60         S=CHIP(RND,D,S-CC)
           CC=CHIP(RND,D,A(J,M)+S)
50    X(J) =CHIP(RND,D,CC/A(J,J))
      WRITE(OUP,7)
      WRITE(OUP,5) ((A(I,J),J=1,M),I=1,N)
      WRITE(OUP,8)
      WRITE(OUP,5) (X(I),I=1,N)
C
C     REFINEMENT BEGINS
      WRITE(OUP,14) (NROW(I),I=1,N)
14    FORMAT(1X,'ROW ORDER',3I2)
C
C     STEP 1
      K=1
C     INITIALIZE XX AT X
      DO 70 I=1,N
70         XX(I)=X(I)
C     STEP 2
500   IF (K.GT.NN) GOTO 600
C          LL IS SET TO 1 IF THE DESIRED ACCURACY IN ANY COMPONENT IS
C          NOT ACHIEVED.  THUS, LL IS INITIALLY 0 FOR EACH ITERATION
           LL=0
C          STEP 3
           DO 80 I=1,N
                R(I)=0.0D+00
C               DO-LOOP IS TO CALCULATE SUMMATION
                DO 90 J=1,N
                     TEMP=CHIP(RND,2*D,B(I,J)*XX(J))
90                   R(I)=CHIP(RND,2*D,R(I)-TEMP)
80              R(I)=CHIP(RND,2*D,B(I,M)+R(I))
           DO 91 I=1,N
91         R(I)=CHIP(RND,D,R(I))
           WRITE(OUP,9) K,(R(I),I=1,N)
C          STEP 4
C          SOLVES THE LINEAR SYSTEM IN THE SAME ORDER AS IN STEP 0
C          THE SOLUTION WILL BE PLACED IN X INSTEAD OF Y
           DO 100 I=1,KKK
                I1=NROW(I)
                KK=I+1
                DO 100 J=KK,N
                J1=NROW(J)
                CC=R(I1)
                CC=CHIP(RND,D,A(J,I)*CC)
                CC=R(J1)-CC
100             R(J1)=CHIP(RND,D,CC)
           CC=R(NROW(N))
           X(N)=CHIP(RND,D,CC/A(N,N))
           DO 110 I=1,KKK
                J=N-I
                JJ=J+1
                S=0
                DO 120 L=JJ,N
                     CC=CHIP(RND,D,A(J,L)*X(L))
120                  S=CHIP(RND,D,S-CC)
                     CC=R(NROW(J))
                     CC=CHIP(RND,D,CC+S)
110             X(J)=CHIP(RND,D,CC/A(J,J))
C          STEPS 5 AND 6
           XXMAX=0.0
           YMAX=0.0
           ERR1=0.0
           DO 130 I=1,N
C               IF NOT ACCURATE THEN LL=1
                IF(DABS(X(I)).GT.TOL) LL=1
                IF(K.EQ.1) THEN
                   IF(DABS(X(I)).GT.YMAX) YMAX=DABS(X(I))
                   IF(DABS(XX(I)).GT.XXMAX) XXMAX=DABS(XX(I))
                ENDIF
                CC=XX(I)
                CCC=CC+X(I)
                XX(I)=CHIP(RND,D,CCC)
                CC=DABS(CC-XX(I))
                IF(CC.GT.ERR1) ERR1=CC
130        CONTINUE
           IF(K.EQ.1) THEN
              COND=YMAX/XXMAX*(10.0D+00)**D
           ENDIF
           WRITE(OUP,11) K,(XX(I),I=1,N)
           IF(LL.EQ.0) THEN
                WRITE(OUP,12) K
                GOTO 401
           END IF
           IF(LL.EQ.2) THEN
              WRITE(OUP,16) TOL
              GOTO 401
           ENDIF
C          STEP 7
           K = K+1
C          STEP 8 IS NOT USED IN THIS IMPLEMENTATION
      GOTO 500
401   WRITE(OUP,92) COND
      GOTO 400
C     STEP 9
C     PROCEDURE COMPLETED UNSUCCESSFULLY
600   CONTINUE
      WRITE(OUP,13) NN
400   CLOSE(UNIT=5)
      CLOSE(UNIT=OUP)
      IF(OUP.NE.6) CLOSE(UNIT=6)
      STOP
4     FORMAT(1X,'ORIGINAL SYSTEM')
5     FORMAT(4(1X,D15.8))
6     FORMAT(1X,'MATRIX SINGULAR - NO UNIQUE SOLUTION')
7     FORMAT(1X,'REDUCED SYSTEM')
8     FORMAT(1X,'GAUSS ELIMINATION GIVES SOLUTION-')
9     FORMAT(1X,'RESIDUAL NO.',I3,' IS',4(1X,D15.8))
11    FORMAT(1X,'ITERATE NO.',I3,' IS',4(1X,D15.8))
12    FORMAT(1X,'SUCCESSFUL APPROXIMATION AFTER ITERATION NO.',I3)
13    FORMAT(1X,'MAXIMUM NUMBER OF ITERATIONS EXCEEDED.')
16    FORMAT(1X,'THE ABOVE VECTOR IS BEST POSSIBLE WITH TOL=',D15.8)
92    FORMAT(1X,'CONDITION NUMBER = ',D15.8)
      END
      DOUBLE PRECISION FUNCTION CHIP(IRND,ND,X)
C     THE FUNCTION CHIP ROUNDS OR CHOPS X TO ND DIGITS
      IMPLICIT REAL*8 (A-H,O-Z)
      INTEGER I
      LOGICAL OK
      DIMENSION TEMP1(5),TN(5),IZZ(5)
      TEN=10.0D+00
      HALF=0.5D+00
      TENTH=0.1D+00
      IF(DABS(X).LT.1.0E-20) THEN
         Z = 0.0D+00
      ELSE
         I=0
         Y=X
         OK=.TRUE.
         Z1=TEN**ND
         Z2=TEN**(ND-1)
         IF(DABS(X).GE.Z1) THEN
100         IF(.NOT.OK) GOTO 101
            Y=Y/TEN
            I=I+1
            IF(DABS(Y).LT.Z1) OK=.FALSE.
            GOTO 100
101         CONTINUE
         ELSE
            IF(DABS(X).LT.Z2) THEN
102            IF(.NOT.OK) GOTO 103
               Y=Y*TEN
               I=I-1
               IF(DABS(Y).GE.Z2) OK=.FALSE.
               GOTO 102
103            CONTINUE
            ENDIF
         ENDIF
         SL=TEN**(-ND)
         IF(IRND.EQ.1) THEN
            IF(Y.GE.0.0) THEN
               TEMP=Y+HALF+TENTH*SL
            ELSE
               TEMP=Y-HALF-TENTH*SL
            ENDIF
         ELSE
            IF(Y.GE.0.0) THEN
               TEMP=Y+TENTH*SL
            ELSE
               TEMP=Y-TENTH*SL
            ENDIF
         ENDIF
         NN=ND/4
         MM=4*NN
         TT=TEMP
         IF(NN.GE.1) THEN
            DO 11 J=1,NN
            TN(J)=TEN**MM
            TEMP1(J)=TT/TN(J)
            IZZ(J)=TEMP1(J)
            TT=TT-IZZ(J)*TN(J)
11          MM=MM-4
         ENDIF
         IZZ(NN+1)=TT
         TN(NN+1)=1
         Z=IZZ(1)*TN(1)
         IF(NN.GE.1) THEN
            NN1=NN+1
            DO 12 J=2,NN1
12          Z=Z+IZZ(J)*TN(J)
         ENDIF
         Z=Z*TEN**I
C         IF(ND.GE.6) THEN
C            ND1=ND/2
C            TEMP1=TEMP/TEN**ND1
C            Z3=INT(TEMP1)
C            TEMP2=TEMP-Z3*TEN**ND1
C            Z4=INT(TEMP2)
C            Z=(Z3*TEN**ND1+Z4)*TEN**I
C         ELSE
C            Z=INT(TEMP)*TEN**I
C         ENDIF
      ENDIF
      CHIP=Z
      RETURN
      END
