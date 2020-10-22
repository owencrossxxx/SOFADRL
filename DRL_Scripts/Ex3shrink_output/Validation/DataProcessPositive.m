%load('results_Ex3_uniform1');


% distance = [distance1,distance2,distance3,distance4];
% pressure = [pressure1,pressure2,pressure3, pressure4];


pressure1(distance1>197|distance1<133)=[];
distance1(distance1>197|distance1<133)=[];
displacement1 = distance1*65/133 - 65;

pressure2(distance2<134)=[];
distance2(distance2<134)=[];
displacement2 = distance2*65/134 - 65;

pressure3(distance3<134)=[];
distance3(distance3<134)=[];
displacement3 = distance3*65/134 - 65;

pressure4(distance4<134)=[];
distance4(distance4<134)=[];
displacement4 = distance4*65/134 - 65;

displacement = [displacement1,displacement2,displacement3,displacement4];
pressure = [pressure1,pressure2,pressure3, pressure4];

rm = (displacement<23 & pressure>7)|(pressure>6&pressure<8&displacement>30.3)|(pressure>2&pressure<4&displacement>20);
displacement(rm)=[];
pressure(rm)=[];
plot(smooth(pressure),smooth(displacement),'.')
xlabel('kPa')
ylabel('mm')
xlim([0 8.5]);

% Linear model Poly5:
%      f(x) = -0.001723*x^5 + 0.03902*x^4 -0.3*x^3 + 0.7705*x^2 + 3.555*x + 0.4403
% Coefficients (with 95% confidence bounds):
%        p1 =   -0.001723  (-0.002056, -0.001389)
%        p2 =     0.03902  (0.032, 0.04603)
%        p3 =        -0.3  (-0.3527, -0.2474)
%        p4 =      0.7705  (0.6042, 0.9368)
%        p5 =       3.555  (3.363, 3.747)
%        p6 =      0.4403  (0.3889, 0.4918)
