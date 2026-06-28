# 511

Date: June 10, 2026
Day: WEDNESDAY
ATTENDANCE: PRESENT
Pair: XAU
DAY RESULT: NO TRADES
HTF Strength: 40.77%
Narrative Achieved: Yes
Comments: Missed trade. 

## Pre Session Notes:
![image.png](511/image.png)
![image.png](511/image%201.png)
![image.png](511/image%202.png)
![image.png](511/image%203.png)
## Session Updates
```javascript
Confluence Factor			Factor Support	Weight
Daily Swing 			Yes	1.0237
Daily Internal 			Yes	0.5615
Daily Fractal			Yes	1.0242
Daily in Internal OTE			No	0.6226
	Structural - Swing		Yes	0.95
4H Swing 			Yes	0.6204
4H Internal 			Yes	1.0236
4H Fractal			Yes	1.1315
4H Price in Swing OTE			No	0.3403
4H Price in Internal OTE			No	0.975
4H Liquidity Sweep - FVG			Yes	1.0754
4H OB Target - Swept Liquidity			Yes	1.0783
4H OB Target - Has Inducement			No	1.4338
4H OB Target - Caused Imbalance			No	0.8691
4H OB Target - Caused Displacement			No	1.062
4H OB Target - Flip Zone			Yes	1.1736
4H OB Target - Within daily OB			No	1.0619
H1 Swing 			Yes	1.0235
H1 Internal 			Yes	0.9262
H1 Fractal			No	1.1315
H1 Price in Swing OTE			No	0.7999
	Previous Candle		Yes	1.4096
H1 Mitigation OB - Has Inducement			Yes	0.7587
H1 Mitigation OB - Caused Imbalance			Yes	1.0239
H1 Mitigation OB - Caused Displacement			Yes	0.9266
H1 Mitigation OB - Flip Zone			No	0.7579
H1 Mitigation OB - Within 4H OB			No	0.8382
	Structural - Fractal		Yes	0.9851
H1 Liquidity Sweep - Asian Liquidity			No	1.1265
	Structural - Internal		Yes	1.0251
	P(t)		40.77	
```
This was a good looking trade by appearance but when calculated comes less than the threshold by a big margin.  The quality got affected due to the 4H OB target which sits above the H1 mitigation OB.  So the price could invalidate the H1 OB and then push up to mitigate the 4H one before actually pushing down.  Thus I considered the 4H taget OB factors.  The same applies to the daily target OB. 
Suppose if I consider the daily target OB, then:
```javascript
Confluence Factor			Factor Support	Weight
Daily Swing 			Yes	1.0237
Daily Internal 			Yes	0.5615
Daily Fractal			Yes	1.0242
Daily in Internal OTE			No	0.6226
	FVG Liquidity		No	1.149
	Previous Candle H/L		No	1.1291
Daily OB Target - Has Inducement			Yes	1.7515
Daily OB Target - Caused Imbalance			Yes	1.5846
Daily OB Target - Caused Displacement			No	1.7513
Daily OB Target - Flip Zone			No	0.8693
	Structural - Swing		Yes	0.95
4H Swing 			Yes	0.6204
4H Internal 			Yes	1.0236
4H Fractal			Yes	1.1315
4H Price in Swing OTE			No	0.3403
4H Price in Internal OTE			No	0.975
4H Liquidity Sweep - FVG			Yes	1.0754
4H OB Target - Swept Liquidity			Yes	1.0783
4H OB Target - Has Inducement			No	1.4338
4H OB Target - Caused Imbalance			No	0.8691
4H OB Target - Caused Displacement			No	1.062
4H OB Target - Flip Zone			Yes	1.1736
4H OB Target - Within daily OB			No	1.0619
H1 Swing 			Yes	1.0235
H1 Internal 			Yes	0.9262
H1 Fractal			No	1.1315
H1 Price in Swing OTE			No	0.7999
	Previous Candle		Yes	1.4096
H1 Mitigation OB - Has Inducement			Yes	0.7587
H1 Mitigation OB - Caused Imbalance			Yes	1.0239
H1 Mitigation OB - Caused Displacement			Yes	0.9266
H1 Mitigation OB - Flip Zone			No	0.7579
H1 Mitigation OB - Within 4H OB			No	0.8382
	Structural - Fractal		Yes	0.9851
H1 Liquidity Sweep - Asian Liquidity			No	1.1265
	Structural - Internal		Yes	1.0251
	P(t)		36.44	
```
Not much of a diffrerence.  The M15 entry model also looks great. It is formed so clean.  But am avoiding this trade as the overall bias is not strong.  
![image.png](511/image%204.png)
![image.png](511/image%205.png)
Price is going in my direction.  Clear winner but did not take the trade. 
## Post Session Notes
The anticipation was that the price would go down during the pre session analysis.  The chart was too good for me to avoid.  Thus initially I avoided the daily OB target which could bring down the probability number.  I also thought of avoiding the 4H OB target as the trade setup looked good from bare eyes.  The one that provoked me the most was the clean entry model.  There was BSLQ engineered and some SSLQ was there.  Thus it was perfect for the price to take the BSLQ and push down and take out the SSLQ — which is what actually happened. 
Previously when there was no probability calculator, when I considred the 4H target OB which is a negative factor, I would think that I am overthinking and would just take the trade as the trade would feel intuitively good.  Now that I am having the calculator, it is taking into account of the 4H OBs which could be a negative factor.  But the factors have weights so this is not an overthinking model.
I accept the missed trade, the calculator has saved me from several losses and this one missed trade could not equalize those positive effects.  Thus I am ending this session with a note that I am not upset with the trading rules and the mechanism.

<!-- synced: 2026-06-10T15:04:00.000Z -->
