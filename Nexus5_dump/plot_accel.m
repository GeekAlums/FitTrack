close all
clear all


data = load('Nexus5Parse.csv');
plot(data(:,1),'r')
hold on
plot(data(:,2),'b')
hold on
plot(data(:,3),'g')

legend('x-axis','y-axis','z-axis')
xlabel('Time in ms')
ylabel('Accl in m/s^2')
grid minor
