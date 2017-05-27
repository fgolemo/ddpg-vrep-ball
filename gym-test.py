import gym

env = gym.make('Pendulum-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print "observation", observation
        print "reward", reward
        print "done", done
        print "info", info
        print "action", action
        print "env.action_space", env.action_space
        print env.action_space.high
        print env.action_space.low
        print("env.observation_space", env.observation_space)
        quit()
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
