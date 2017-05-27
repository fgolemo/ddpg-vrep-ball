import matplotlib.pyplot as plt
import numpy as np

RUN = 1
SETTING = "biggerOuNoise"

rewards = np.loadtxt("rewards/rewards-{}-{}.log".format(SETTING, RUN), dtype=np.float32)
x = np.arange(len(rewards))

plt.plot(x, rewards)
# plt.show()
plt.savefig('figures/figure-{}-{}.png'.format(SETTING, RUN))
