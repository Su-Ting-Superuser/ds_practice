import numpy as np


SAMPLE_SPACE_PEOPLE = ['D', 'N']    # D: drug user, N: none drug user
SAMPLE_SPACE_TESTS = ['+', '-']     # +: possitive test, -: negative test

TEST_SENSITIVITY = 0.99     # rate of true positive
TEST_SPECIFICITY = 0.99     # rate of true negative

P_DRUG_USER = 0.005         # percentage of drug users within the population


def run_simulation(
        population_size: int = 10000,
        sensitivity: float = TEST_SENSITIVITY,
        specificity: int = TEST_SPECIFICITY,
):
    """run_simulation"""

    population = generate_population(population_size, P_DRUG_USER)
    test_results = apply_drug_tests(population, sensitivity, specificity)

    n_drug_user = np.count_nonzero(population == 'D')
    n_positive_test = np.count_nonzero(test_results == '+')
    p_being_drug_user_with_positive_test = n_drug_user / n_positive_test

    print(f"========== Running simulation ==========")
    print(f"population: {population_size}, sensitivity: {sensitivity}, specificity: {specificity}")
    print(f"Number of drug users: {n_drug_user}")
    print(f"Number of possitive tests: {n_positive_test}")
    print(f"Probability of being a real drug user with a positive test: {p_being_drug_user_with_positive_test}")

    return p_being_drug_user_with_positive_test


def generate_population(size: int, p_drug_user: float = P_DRUG_USER):
    """
    generate a population of `size` people, where P_drug_user * 100% of it are drug users

    Args:
        size(int): population size
        p_drug_user(float): persentage of drug users

    Returns:
        population(np.array): generated population
    """
    population = np.random.choice(SAMPLE_SPACE_PEOPLE, size, p=[p_drug_user, 1 - p_drug_user])

    return population


def apply_drug_tests(
        population: np.array,
        sensitivity: float = TEST_SENSITIVITY,
        specificity: float = TEST_SPECIFICITY,
):
    """
    apply drug tests to the population

    Args:
        population(np.array): array of people
        sensitivity(float): rate of true positive, probability of yielding positive result(+) to a drug user(D)
        specificity(float): rate of true negative, probability of yielding negative result(-) to a none drug user(N)

    Returns:
        results(np.array): test results of the population
    """
    def _test_people(people: np.array):
        results = []
        for person in people:
            if person == 'D':
                result = np.random.choice(SAMPLE_SPACE_TESTS, 1, p=[sensitivity, 1 - sensitivity])
            else:
                result = np.random.choice(SAMPLE_SPACE_TESTS, 1, p=[1 - specificity, specificity])
            results.append(result[0])
        return results

    results = np.apply_along_axis(_test_people, 0, population)

    return results




if __name__ == "__main__":
    run_simulation()
