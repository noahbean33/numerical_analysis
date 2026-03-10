function [maxx,maxerr]=UniformInterp(a,b,n)

%% Nodes and function values
h=(b-a)/n; x=a:h:b; y=f(x);

%% Uniform weights
wt=zeros(1,n+1);
wt(1)=1;
for k=1:n
    wt(k+1:-1:2)=wt(k+1:-1:2)+wt(k:-1:1);
end
wt(2:2:n+1)=-wt(2:2:n+1);

%% Evaluation points
m=4; hh=h/m; xx=a:hh:b;

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
