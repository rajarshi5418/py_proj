import mibian
print(dir(mibian.BS))

underlying_price = 8572
call_strike = 8700
put_strike = 8500
call_price = 616.05
put_price = 654.05
interest_rate = 0
call_implied_volatility = 67.50
put_implied_volatility = 69.20
days_to_expiry = 31


# Calculating CALL PREMIUM
# mibian.BS([underlyingPrice, callStrikePrice, interestRate, daysToExpiration], volatility)
c = mibian.BS([15600, 16000, 10, 10], volatility = 16.50)
print(c.callPrice)
print(c.callDelta)
print(c.callTheta)
print(c.vega)
print(c.gamma)

# Calculating PUT PREMIUM
# mibian.BS([underlyingPrice, putStrikePrice, interestRate, daysToExpiration], volatility)
p = mibian.BS([8572, 8500, 0, 31], volatility = 69.20)
print(p.putPrice)
print(p.putDelta)
print(p.putTheta)
print(p.vega)
print(p.gamma)

# Calculating CALL Implied Volatility
# mibian.BS([underlyingPrice, callStrikePrice, interestRate, daysToExpiration], callPrice)
c = mibian.BS([8572, 8700, 0, 31], callPrice= 614.56)
print(c.impliedVolatility)

# Calculating PUT Implied Volatility
# mibian.BS([underlyingPrice, putStrikePrice, interestRate, daysToExpiration], putPrice)
p = mibian.BS([8572, 8500, 0, 31], putPrice= 650.20)
print(p.impliedVolatility)

# Calculating CALL Delta
c = mibian.BS([8572, 8700, 0, 31], volatility= 67.65)
print(c.callDelta)

# Calculating PUT Delta
p = mibian.BS([8572, 8500, 0, 31], volatility= 69.59)
print(p.putDelta)


# Calculating CALL Theta
c = mibian.BS([8572, 8700, 0, 31], volatility= 67.65)
print(c.callTheta)

# Calculating Put Theta
p = mibian.BS([8572, 8500, 0, 31], volatility= 69.59)
print(p.putTheta)

# Calculating CALL Vega
c = mibian.BS([8572, 8700, 0, 31], volatility= 67.65)
print(c.vega)

# Calculating Put Vega
p = mibian.BS([8572, 8500, 0, 31], volatility= 69.59)
print(p.vega)

# Calculating CALL Gamma
c = mibian.BS([8572, 8700, 0, 31], volatility= 67.65)
print(c.gamma)

# Calculating Put Gamma
p = mibian.BS([8572, 8500, 0, 31], volatility= 69.59)
print(p.gamma)

# Calculating Putcall Parity
c = mibian.BS([8572, 8700, 0, 31], callPrice=614.56, putPrice=745)
print(c.putCallParity)

