import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    lcm = denom1 * denom2 // math.gcd(denom1, denom2)
    sum_numer = numer1 * (lcm  // denom1) + numer2 * (lcm // denom2)
    gcd_value = math.gcd(sum_numer, lcm)
    
    return [sum_numer // gcd_value, lcm // gcd_value]