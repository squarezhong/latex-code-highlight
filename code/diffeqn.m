function y = diffeqn(a,x,yn1)
    y = zeros(1, length(x));
    y(1) = a .* yn1 + x(1);
    for n = 2:length(y)
        y(n) = a.*y(n-1) + x(n);
    end

   