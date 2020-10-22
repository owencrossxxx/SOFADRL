close all
load('NegativeData')
pressureSim = table2array(pressurevspositionuniformnegative(:,2))*100;
distanceSim = table2array(pressurevspositionuniformnegative(:,1));
displacementSim = distanceSim -71.485;

figure

plot(pressureSim,displacementSim,'ob','MarkerSize',2)
xlabel('kPa')
ylabel('mm')
%xlim([0 8.5])
hold on


plot(pressure,displacement,'or','MarkerSize',2)
xlabel('kPa')
ylabel('mm')
%xlim([0 8.5])
%ylim([0 40])

% Lpressure = (0:0.001:8);
% LdisplacementReal = -0.001723*Lpressure.^5 + 0.03902*Lpressure.^4 -0.3*Lpressure.^3 + 0.7705*Lpressure.^2 + 3.555*Lpressure + 0.4403;
% LdisplacementSim = -0.2304*Lpressure.^2 + 5.59*Lpressure +0.8658;
% 
% subplot(2,2,3)
% plot(Lpressure,LdisplacementSim,'b','MarkerSize',2)
% xlabel('kPa')
% ylabel('mm')
% hold on
% 
% plot(Lpressure,LdisplacementReal*1.205,'r','MarkerSize',2)
% legend('Sim','Real','Location','northwest')
% xlim([0 8.5])