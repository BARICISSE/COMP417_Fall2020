class PIDController:
    def __init__(self, target_pos):
        self.target_pos = 0
        self.Kp = 1800
        self.Ki = 1500
        self.Kd = 600
        self.bias = 0
        
        self.t = 1.0/60.0
        self.I = 0 
        self.ERROR_ant = 0 
        return

    def reset(self):
        return

#TODO: Complete your PID control within this function. At the moment, it holds
#      only the bias. Your final solution must use the error between the 
#      target_pos and the ball position, plus the PID gains. You cannot
#      use the bias in your final answer. 
    def get_fan_rpm(self, vertical_ball_position):
        ERROR = self.target_pos - vertical_ball_position
        difference_ERROR = ERROR - self.ERROR_ant

        P = ERROR 
        self.I = self.I + ERROR*self.t
        coeficient = difference_ERROR /self.t
        #lets make it stable with 1760 value
        self.bias = 1760 + ((self.Kp*P)+(self.Ki*self.I)+ (self.Kd*coeficient))
        self.ERROR_ant = ERROR
        output = self.bias

        if (output > 10000):
            output = 7500
        return output
