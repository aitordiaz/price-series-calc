"""Module that calculates the price series of a synthetic index
"""
import numpy as np


def compute_price(data, t):
    """A synthetic index is an aggregate of some underlying securities;
    each security is assigned a weight in the index to get the price of the
    synthetic index for each date, which is calculated according to this
    function

    :param data: Dataframe with dates, weights and underlying securities for
        each date
    :param t: Date for which the price has to be computed
    :return:
    :rtype:
    """
    if t == 0:
        return 100
    else:
        return compute_price(data, t - 1) * (1 + compute_returns(data, t))


def compute_returns(data, t):
    """Computes return of the index on date t

    :param data: Weight and prices of the underliying securities
        needed for the calculation of the index
    :param t: Date for
    :return:
    :rtype:
    """
    weight = data.iloc[0, t]
    prices = data.iloc[1:, t-1:t+1]
    underliying_securities = compute_underlying_securities(prices, t)
    return np.sum(weight * underliying_securities)


def compute_underlying_securities(prices, t):
    """Computes return of each underlying security on date t

    :param prices: Underliying securities prices series for t and t-1 dates
    :param t: Date for which return has to be computed
    :return: Series with return of each underlying security on date t
    :rtype:
    """
    return prices[t] / prices[t-1] - 1
