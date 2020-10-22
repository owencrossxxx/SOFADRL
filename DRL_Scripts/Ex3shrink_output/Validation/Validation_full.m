close all

pressureSim = table2array(pressurevspositionuniform4full(:,2))*100;
distanceSim = table2array(pressurevspositionuniform4full(:,1));
displacementSim = distanceSim -71.48;

LpressureSim = (0:0.01:10);
LdisplacementSim = 0.009087*LpressureSim.^3-0.3584*LpressureSim.^2 + 6.105*LpressureSim + 0.3357;

LpressureReal = (0:0.01:10);
LdisplacementReal = 0.01002*LpressureReal.^3 -0.239*LpressureReal.^2 + 5.015*LpressureReal + 1.664;

pressureReal = table2array(resultsEx3uniformreal(:,1));
distanceReal = table2array(resultsEx3uniformreal(:,2))*65*1.02/153;
displacementReal = distanceReal - 64;

figure
subplot(2,2,1)
plot(pressureSim,displacementSim,'ob','MarkerSize',2)
xlabel('kPa')
ylabel('mm')

subplot(2,2,2)
plot(pressureReal,displacementReal,'or','MarkerSize',2)
xlabel('kPa')
ylabel('mm')


subplot(2,2,3)
plot(LpressureSim,LdisplacementSim,'b','MarkerSize',2)
xlabel('kPa')
ylabel('mm')
hold on

plot(LpressureReal,LdisplacementReal,'r','MarkerSize',2)
legend('Sim','Real','Location','northwest')


% meanError = mean(displacementSim -displacementReal);
% fprintf('Mean error = %f\n',meanError);

RMSE = sqrt(mean((displacementSim -displacementReal).^2));
%disp(RMSE)
fprintf('RMSE = %f\n',RMSE);
R = corrcoef(displacementSim,displacementReal);
%disp(R(1,2))
fprintf('Correlation coefficient = %f\n',R(1,2));
