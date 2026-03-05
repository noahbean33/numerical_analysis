function [maxx,maxerr]=ChebyshevInterp(a,b,n)

%% Nodes and function values
mid=(a+b)/2; rad=(b-a)/2;
x=mid+rad*cos(pi*(0:1/n:1)); y=f(x);

%% Chebyshev weights
wt=ones(1,n+1);
wt(2:2:n+1)=-wt(2:2:n+1);
wt(1)=wt(1)/2; wt(n+1)=wt(n+1)/2;

%% Evaluation points
m=4; hh=(b-a)/(m*n); xx=a:hh:b;

figure(1);
yf=f(xx);
yp=p(xx,x,y,wt);
plot(xx,yp,'o-',xx,yf,'v-');
err=abs(yf-yp);
figure(2);
plot(xx,err,'s-');
[maxerr,maxi]=max(err); maxx=xx(maxi);

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=f(x)

val=1./(1+25*x.*x);

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=p(xx,x,y,wt)

dd=1./(xx-x');
[I,J]=find(isinf(dd));
denom=wt*dd;
numer=(wt.*y)*dd;
val=numer./denom;
val(J)=y(I);

end
