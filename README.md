[![Build Status](https://travis-ci.org/desnoe/alcoholo.svg?branch=master)](https://travis-ci.org/desnoe/alcoholo)

# Alcoholo python module

This python module calculates the alcoholometric table as defined in the specification R022-f75 (see doc folder -
in french!) defined by the OIML.

## Examples

Determine the density (in kg/m3) of a mixture of water and ethanol from the alcoholic strength by mass (for example
50%) and from the temperature (at 20°C for example):

```
from alcoholo.tables import rho_p_t
rho_p_t(0.5, 20.0)
```
