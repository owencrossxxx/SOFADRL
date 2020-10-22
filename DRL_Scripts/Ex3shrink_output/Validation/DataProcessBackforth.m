pressure(distance<120|distance>200|distance<0)=[];
distance(distance<120|distance>200|distance<0) = [];

displacement= (distance*65/123 -65);
plot(pressure,displacement*1.205,'.')

xlabel('kPa')
ylabel('mm')
xlim([0 8.5])
ylim([0 inf])