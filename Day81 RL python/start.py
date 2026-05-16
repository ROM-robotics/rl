from stable_baselines3 import PPO
import gymnasium as gym

# ၁။ Environment တည်ဆောက်ခြင်း
env = gym.make("CartPole-v1")

# ၂။ Model/Algorithm ရွေးချယ်ခြင်း (Optimal Policy ရှာရန်)
model = PPO("MlpPolicy", env, verbose=1)

# ၃။ Training လုပ်ခြင်း (Bellman Optimality ကို အခြေခံပြီး သင်ယူခြင်း)
model.learn(total_timesteps=10000)

# ၄။ ရလဒ်ကို အသုံးပြုခြင်း
obs, _ = env.reset()
action, _ = model.predict(obs) # အကောင်းဆုံး action ကို ထုတ်ပေးခြင်း