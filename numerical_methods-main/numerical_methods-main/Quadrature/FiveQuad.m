function [L,R,T,M,S]=FiveQuad(a,b,n)

h=(b-a)/n; 
x=a:h:b; 
y=(a+h/2):h:(b-h/2);

fx=f(x);
fy=f(y);

L=h*sum(fx(1:n)); 
R=h*sum(fx(2:n+1));
T=(L+R)/2; 
M=h*sum(fy); 
S=(2*M+T)/3;

end

function y=f(x)
    y=sqrt(x);
end
