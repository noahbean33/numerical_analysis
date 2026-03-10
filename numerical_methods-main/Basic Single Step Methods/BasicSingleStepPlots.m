function BasicSingleStepPlots(h)

t0=0; tf=pi; tt=t0:h:tf; m=length(tt);

% Initialization
yy=zeros(1,m); yyt=zeros(1,m);
k=1; t=t0; yy(k)=TrueSol(t); yyt(k)=TrueSol(t);

for k=1:m-1
    yy(k+1)=M(tt(k),h,yy(k)); 
    yyt(k+1)=TrueSol(tt(k+1)); 
end

figure(1); plot(tt,yy,'o');
figure(2); plot(tt,yyt-yy,'x');

end % BasicSingleStep

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=f(t,y)
    
    %val=-0.25*t*y;
    val=y*(1-y);
    
end % f

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=df(t,y)
% Derivative of f in its second argument    
    
    %val=-0.25*t;
    val=1-2*y;
    
end % df

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=TrueSol(t,y)
% Derivative of f in its second argument    
    
    %val=exp(-0.125*t*t);
    val=exp(t)/(1+exp(t));
    
end % TrueSol


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=FE(t,h,y)
     
    val=y+h*f(t,y);
    
end % FE

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=TPC(t,h,y)
     
    z=y+h*f(t,y);
    val=y+0.5*h*(f(t,y)+f(t+h,z));
    
end % TPC

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=M(t,h,y)
     
    z=y+0.5*h*f(t,y);
    val=y+h*f(t+h/2,z);
    
end % M

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=BE(t,h,y)
     
    jmax=2; z=y;
    for j=1:jmax
        z=z-(y+h*f(t+h,z)-z)/(h*df(t+h,z)-1);
    end
    val=z;
    
end % BE

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function val=T(t,h,y)
     
    jmax=2; z=y;
    for j=1:jmax
        z=z-(y+0.5*h*(f(t,y)+f(t+h,z))-z)/(0.5*h*df(t+h,z)-1);
    end
    val=z;
    
end % T
