import numpy as np
import socket
import gym, ray
from ray.rllib.agents import ppo
import math

sock = socket.socket()
sock.connect(('127.0.0.1',12345))



class MyEnv(gym.Env):

    def __init__(self, env_config):
        #self.action_space = <gym.Space>
        #self.observation_space = <gym.Space>
        pass
        
    def reset(self):
        self.goal = 80 + np.random.rand()*10
        self.step_counter = 0
        reset = "reset"
        sock.send(reset.encode())
        s = np.array([float(sock.recv(1024).decode())])
        return s

    def step(self, action):
        
        sock.send(action.encode())
        s = float(sock.recv(1024).decode())
        
        reward = self.compute_reward(self.goal,s)
        self.step_counter += 1
        done = self.check_if_epsiode_steps_complete(self.step_counter,100)

        return s, reward, done, "additional info"
    
    
    def compute_reward(self, goal,s):
        r = self.logistic_kernel((s - goal))
        return r

    def logistic_kernel(self, x):
        return 1 / (math.exp(x) + 2 + math.exp(-x))

    def check_if_epsiode_steps_complete(self, step_counter, n):
    
        if step_counter >= n:
            done = True
        else:
            done = False
        
        return done




        

ray.init()
trainer = ppo.PPOTrainer(env=MyEnv, config={
    "env_config": {},  # config to pass to env class
})

while True:
    print(trainer.train())

