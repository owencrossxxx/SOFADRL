pressure5(distance5>133)=[];
distance5(distance5>133)=[];
displacement5 = distance5*65/133 - 65;

pressure6(distance6>133)=[];
distance6(distance6>133)=[];
displacement6 = distance6*65/133 - 65;


displacement = [displacement5,displacement6];
pressure = [pressure5,pressure6];

rm = (displacement<-55|(pressure<-2&displacement>-40)|pressure< -9|pressure>-0.45);
displacement(rm)=[];
pressure(rm)=[];
plot(smooth(pressure),smooth(displacement),'.')
xlabel('kPa')
ylabel('mm')
xlim([-9 0]);
% figure
% subplot(2,1,1)
% plot(smooth(pressure5),smooth(displacement5),'.')
% subplot(2,1,2)
% plot(smooth(pressure6),smooth(displacement6),'.')

% Linear model Poly6:
%      f(x) = p1*x^6 + p2*x^5 + p3*x^4 + p4*x^3 + p5*x^2 + 
%                     p6*x + p7
% Coefficients (with 95% confidence bounds):
%        p1 =    0.009981  (0.008826, 0.01114)
%        p2 =      0.3304  (0.2952, 0.3655)
%        p3 =       4.314  (3.898, 4.73)
%        p4 =       28.14  (25.74, 30.55)
%        p5 =       95.62  (88.69, 102.5)
%        p6 =       160.8  (151.7, 169.8)
%        p7 =       60.92  (56.9, 64.93)