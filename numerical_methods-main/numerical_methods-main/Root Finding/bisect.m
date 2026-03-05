function [n,x,fx,d]=bisect(a,b)

nmax=100; tol=1.0e-8;

fa=f(a); fb=f(b);
if(fa*fb >= 0)
    disp('Bad search interval');
    x=NaN; fx=NaN; n=0; d=NaN;
    return;
end

x=(a+b)/2; fx=f(x); n=0; d=(b-a)/2;
while(n <= nmax & abs(fx)>tol & d>tol)
    if(fa*fx<0)
        b=x;fb=fx;
    else
        a=x;fa=fx;
    end
    x=(a+b)/2; fx=f(x); n=n+1; d=d/2;
end

function y=f(x)

y=(3*x-2)*(x*x+1);
