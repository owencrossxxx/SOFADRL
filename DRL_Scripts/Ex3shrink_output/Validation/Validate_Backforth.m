close all
load('PositiveData')
pressureSim = table2array(pressurevsposition_uniform_backforth1(:,2))*100;
distanceSim = table2array(pressurevsposition_uniform_backforth1(:,1));
displacementSim = distanceSim -71.485;

figure
subplot(2,2,1)
plot(pressureSim,displacementSim,'ob','MarkerSize',2)
xlabel('kPa')
ylabel('mm')
xlim([0 8.5])


subplot(2,2,2)
plot(pressure,displacement*1.205,'or','MarkerSize',2)
xlabel('kPa')
ylabel('mm')
xlim([0 8.5])
ylim([0 40])

Lpressure = (0:0.001:8);
LdisplacementReal = -0.001723*Lpressure.^5 + 0.03902*Lpressure.^4 -0.3*Lpressure.^3 + 0.7705*Lpressure.^2 + 3.555*Lpressure + 0.4403;
LdisplacementSim = -0.2304*Lpressure.^2 + 5.59*Lpressure +0.8658;

subplot(2,2,3)
plot(Lpressure,LdisplacementSim,'b','MarkerSize',2)
xlabel('kPa')
ylabel('mm')
hold on

plot(Lpressure,LdisplacementReal*1.205,'r','MarkerSize',2)
legend('Sim','Real','Location','northwest')
xlim([0 8.5])