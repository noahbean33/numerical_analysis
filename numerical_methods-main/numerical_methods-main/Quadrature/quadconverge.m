format short e % formatting

a=0; b=1; % Endpoints of interval

% e - 1 (exact value of integral)
I=(2/3);

% zero matrix with m rows, 15 columns
m=8; E=zeros(m,15);

% Errors for five methods in columns
% J=1:3:13=[1,4,7,10,13]
J=1:3:13; n=1;
for k=1:m
    [L,R,T,M,S]=FiveQuad(a,b,n);
    E(k,J)=I-[L,R,T,M,S];
    n=2*n;
end

% Error ratios for five methods in
% columns K=2:3:14=[2,5,8,11,14]
K=2:3:14;
E(2:m,K)=abs(E(1:m-1,J)./E(2:m,J));

% Estimates of order of convergence in
% columns LL=3:3:15=[3,6,9,12,15]
LL=3:3:15;
E(2:m,LL)=log(E(2:m,K))/log(2);
