function emax=BasicSingleStep(h)

t0=0; tf=5;

% Initialization
t=t0; y=TrueSol(t0); emax=0;

while(t+h<=tf)
   y=FE(t,h,y); 
   t=t+h; 
   emax=max(emax,abs(TrueSol(t)-y));
end

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
