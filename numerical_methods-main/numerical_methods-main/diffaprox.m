function [final] = diffaprox()

fprime = 1/4;
c = sqrt(3);
eL = zeros(53,1);
eR = zeros(53,1);
eC = zeros(53,1);
hvect = zeros(53,1);
kvect = zeros(53,1);

for k = 1:53
    h = 2^(-(k-1));
    fcmh = fun(c-h);
    fcph = fun(c+h);
    fc = fun(c);

    foleft = (fc - fcmh) / h;
    foright = (fcph - fc) / h;
    socenter = (fcph - fcmh) / (2*h);

    eL(k,:) = abs(foleft - fprime);
    eR(k,:) = abs(foright - fprime);
    eC(k,:) = abs(socenter - fprime);
    hvect(k,:) = h;
    kvect(k,:) = k;

    format short e
    final = [kvect, hvect, eL, eR, eC];
    
end

end

function f = fun(c)
    f = atan(c);
end