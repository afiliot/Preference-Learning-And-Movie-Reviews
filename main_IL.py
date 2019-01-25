import Instance_learning as IL
import numpy as np
import input_data as data
import expe as xp
import utils

np.random.seed(42311)

check_random = False
check_real_data = True

if __name__ == '__main__':
    if check_random:
        alpha = np.array([1/10.]*10)
        n, d, m, mp = 20, 10, 100, 200
        generator = data.instance_pref_generator(func=data.cobb_douglas, func_param=alpha)
        train, test = generator.sample_datasets(n, d, m, mp)
        K, sigma = 10., 0.1
        model = IL.learning_instance_preference(inputs=train, K=K, sigma=sigma)
        xp.xp_random_dataset(generator, model, train, test, K, sigma, gridsearch=False)

    if check_real_data:
        generator = data.pref_generator('diabetes')
        train = generator.get_input(200)
        test = generator.draw_preference(generator.train_test_generator(800))
        K, sigma = 10., 0.1
        model = IL.learning_instance_preference(inputs=train, K=K, sigma=sigma)
        xp.xp_random_dataset(generator, model, train, test, K, sigma, gridsearch=False)

