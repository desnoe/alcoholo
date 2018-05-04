[![Build Status](https://travis-ci.org/desnoe/alcoholo.svg?branch=master)](https://travis-ci.org/desnoe/alcoholo)

*Read this in other languages: [French](README.fr.md).*

# Alcoholo python3 module

This python3 module calculates the alcoholometric table as defined in the specification R022-e75 (see doc folder)
defined by the OIML.

## Installation

```
git clone https://github.com/desnoe/alcoholo.git
cd alcoholo
python3
```

## Examples

Determine the density (in kg/m3) of a mixture of water and ethanol from the alcoholic strength by mass (for example
50%) and from the temperature (at 20°C for example):

```pycon
>>> from alcoholo.tables import rho_p_t
>>> rho_p_t(0.5, 20.0)
913.7705950261712
```
