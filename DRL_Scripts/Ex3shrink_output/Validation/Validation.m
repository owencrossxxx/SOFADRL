close all

%pressureSim = table2array(pressurevspositionuniform4(:,2))*100;
%distanceSim = table2array(pressurevspositionuniform4(:,1));

%LpressureSim = (1:0.1:10);
%LdistanceSim = -0.1989*LpressureSim.^2 + 5.266*LpressureSim + 73.08;

%pressureReal = table2array(resultsEx3uniform1(:,1));
%distanceReal = table2array(resultsEx3uniform1(:,2))*65*1.1/140;



pressureReal = pressure;
distanceReal = distance*65*1.1/140 - 71.4;

figure
%plot(LpressureSim,LdistanceSim)


hold on
plot(pressureReal,distanceReal,'or','MarkerSize',2)
xlabel('kPa')
ylabel('mm')
%legend('Sim','Real','Location','northwest')

%RMSE = sqrt(mean((distanceReal +0.1989*pressureReal.^2 - 5.266*pressureReal - 73.08).^2));
%disp(RMSE)
% Sim Linear model Poly2:
%      f(x) = p1*x^2 + p2*x + p3
% Coefficients (with 95% confidence bounds):
%        p1 =     -0.1989  (-0.1997, -0.1981)
%        p2 =       5.266  (5.256, 5.275)
%        p3 =       73.08  (73.06, 73.11)