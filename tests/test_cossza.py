import sys

from context import thermofeel
from math import cos, pi, radians

def main():
    
    # should return ~ 0.360303587797559
    cossza = thermofeel.calculate_cos_solar_zenith_angle(
        lat=48.81667, lon=2.28972, d=15, m=11, y=2006, h=10.58333)
    
    assert abs(cossza - 0.360303587797559) < 1e-6

    # London, ~ 0.8799471697555967
    cossza = thermofeel.calculate_cos_solar_zenith_angle(
        lat=51.0, lon=0.0, d=4, m=6, y=2021, h=12.0)

    assert abs(cossza - 0.8799471697555967) < 1e-6

    # from alternative formula
    assert abs(cossza - cos(radians(90.0 - 61.5))) < 1e-2

if __name__ == "__main__":
    sys.exit(main())