%% Second order 
% Mean Defuzzification

clc
clear
close all

alpha = -1;
beta = 1;

h = 0.25;
N = 9;

x1 = alpha:0.01:beta;
x2 = alpha:0.01:beta;
[x1, x2] = meshgrid(x1, x2);

g_bar = zeros(N*N, 1);
e_i1 = zeros(N, 1);
e_i2 = zeros(N, 1);

num = 0;
den = 0;
k = 1;

% triangular fuzzy membership function
trimf = @(x, abc) max(min((x - abc(1)) / (abc(2) - abc(1)), (abc(3) - x) / (abc(3) - abc(2))), 0);

for i1 = 2:N
    for i2 = 2:N
        e_i1(i1-1,1) = -1 + h*(i1-2);
        e_i2(i2-1,1) = -1 + h*(i2-2);
        if i1 == 2
            mu_A_x1 = trimf(x1, [-1, -1, -1+h]);
        elseif i1 == N
            mu_A_x1 = trimf(x1, [1-h, 1, 1]);
        else
            mu_A_x1 = trimf(x1, [-1+h*(i1-3), -1+h*(i1-2), -1+h*(i1-1)]);
        end
        if i2 == 2
            mu_A_x2 = trimf(x2, [-1, -1, -1+h]);
        elseif i2 == N
            mu_A_x2 = trimf(x2, [1-h, 1, 1]);
        else
            mu_A_x2 = trimf(x2, [-1+h*(i2-3), -1+h*(i2-2), -1+h*(i2-1)]);
        end
        g_bar(k,1) = 1 / (3 + e_i1(i1-1,1) + e_i2(i2-1,1));
        num = num + g_bar(k,1) * mu_A_x1 .* mu_A_x2;
        den = den + mu_A_x1 .* mu_A_x2;
        k = k + 1;
    end
end

f_x = num ./ den;
g_x = 1 ./ (3 + x1 + x2);

figure(1)
surf(x1, x2, g_x, 'FaceColor', 'b', 'EdgeColor', 'none')
xlabel('$x_1$', 'Interpreter', 'latex')
ylabel('$x_2$', 'Interpreter', 'latex')
zlabel('g(x)', 'Interpreter', 'latex')
legend('$g(x)$', 'Interpreter', 'latex')
grid on

figure(2)
surf(x1, x2, f_x, 'FaceColor', 'r', 'EdgeColor', 'none')
xlabel('$x_1$', 'Interpreter', 'latex')
ylabel('$x_2$', 'Interpreter', 'latex')
zlabel('f(x)', 'Interpreter', 'latex')
legend('$f(x)$', 'Interpreter', 'latex')
grid on

figure(3)
surf(x1, x2, g_x - f_x, 'EdgeColor', 'none')
xlabel('$x_1$', 'Interpreter', 'latex')
ylabel('$x_2$', 'Interpreter', 'latex')
zlabel('Error', 'Interpreter', 'latex')
title('Error', 'Interpreter', 'latex')
colorbar
grid on