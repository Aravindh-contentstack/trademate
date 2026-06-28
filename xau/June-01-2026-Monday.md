# 504

Date: June 1, 2026
Day: MONDAY
ATTENDANCE: PRESENT
Pair: XAU
DAY RESULT: NO TRADES
HTF Strength: 50.87%
Narrative Achieved: Yes
Comments: Price went in our direction but no trades for us. 

## Pre Session Notes:
![image.png](504/image.png)
![image.png](504/image%201.png)
![image.png](504/image%202.png)
![image.png](504/image%203.png)
## Session Updates
```javascript
Confluence Factor			Factor Support	Weight
Daily Swing 			Yes	1.0237
Daily Internal 			Yes	0.5615
Daily Fractal			No	1.0242
Daily in Internal OTE			Yes	0.6226
Daily Liquidity Sweep - Equals			Yes	1.0474
Daily Liquidity Sweep - FVG			Yes	1.5166
	Structural - Internal		Yes	1
	Structural - Fractal		Yes	0.9751
4H Swing 			Yes	0.6204
4H Internal 			No	1.0236
4H Fractal			Yes	1.1315
4H Price in Swing OTE			Yes	0.3403
4H Price in Internal OTE			No	0.975
4H Mitigation OB - Swept Liquidity			No	1.0887
4H Mitigation OB - Has Inducement			No	1.1535
4H Mitigation OB - Caused Imbalance			No	0.9442
4H Mitigation OB - Caused Displacement			Yes	1.2743
4H Mitigation OB - Flip Zone			Yes	0.8543
4H Mitigation OB - Within daily OB			No	0.7361
	Structural - Swing		Yes	1.05
	Structural - Internal		No	0.9975
4H Liquidity Sweep - Equals			Yes	1.0447
4H Liquidity Sweep - FVG			No	1.0754
4H Liquidity Target - FVG Liquidity			Yes	1.3418
H1 Swing 			No	1.0235
H1 Internal 			Yes	0.9262
H1 Fractal			Yes	1.1315
H1 Price in Swing OTE			Yes	0.7999
	Previous Candle		Yes	1.4096
H1 Mitigation OB - Has Inducement			Yes	0.7587
H1 Mitigation OB - Caused Imbalance			Yes	1.0239
H1 Mitigation OB - Caused Displacement			Yes	0.9266
H1 Mitigation OB - Flip Zone			Yes	0.7579
H1 Mitigation OB - Within 4H OB			Yes	0.8382
	Structural - Old points		No	1.0474
H1 Liquidity Sweep - PDH/PDL			No	1.1709
	Structural - Fractal		Yes	1.1148
H1 Liquidity Target - FVG Liquidity			Yes	1.129
	P(t)		50.24	
```
I did not add the 4H OB target for the above, if I add that:
```javascript
Confluence Factor			Factor Support	Weight
Daily Swing 			Yes	1.0237
Daily Internal 			Yes	0.5615
Daily Fractal			No	1.0242
Daily in Internal OTE			Yes	0.6226
Daily Liquidity Sweep - Equals			Yes	1.0474
Daily Liquidity Sweep - FVG			Yes	1.5166
	Structural - Internal		Yes	1
	Structural - Fractal		Yes	0.9751
4H Swing 			Yes	0.6204
4H Internal 			No	1.0236
4H Fractal			Yes	1.1315
4H Price in Swing OTE			Yes	0.3403
4H Price in Internal OTE			No	0.975
4H Mitigation OB - Swept Liquidity			No	1.0887
4H Mitigation OB - Has Inducement			No	1.1535
4H Mitigation OB - Caused Imbalance			No	0.9442
4H Mitigation OB - Caused Displacement			Yes	1.2743
4H Mitigation OB - Flip Zone			Yes	0.8543
4H Mitigation OB - Within daily OB			No	0.7361
	Structural - Swing		Yes	1.05
	Structural - Internal		No	0.9975
4H Liquidity Sweep - Equals			Yes	1.0447
4H Liquidity Sweep - FVG			No	1.0754
	Structural - Internal		Yes	1.0448
4H OB Target - Has Inducement			Yes	1.4338
4H OB Target - Caused Imbalance			Yes	0.8691
4H OB Target - Caused Displacement			Yes	1.062
4H OB Target - Flip Zone			No	1.1736
4H OB Target - Within daily OB			No	1.0619
4H Liquidity Target - FVG Liquidity			Yes	1.3418
H1 Swing 			No	1.0235
H1 Internal 			Yes	0.9262
H1 Fractal			Yes	1.1315
H1 Price in Swing OTE			Yes	0.7999
	Previous Candle		Yes	1.4096
H1 Mitigation OB - Has Inducement			Yes	0.7587
H1 Mitigation OB - Caused Imbalance			Yes	1.0239
H1 Mitigation OB - Caused Displacement			Yes	0.9266
H1 Mitigation OB - Flip Zone			Yes	0.7579
H1 Mitigation OB - Within 4H OB			Yes	0.8382
	Structural - Old points		No	1.0474
H1 Liquidity Sweep - PDH/PDL			No	1.1709
	Structural - Fractal		Yes	1.1148
H1 Liquidity Target - FVG Liquidity			Yes	1.129
	P(t)		50.87	
```
In both the cases the trade probability is above the threshold.  
![image.png](504/image%204.png)
```javascript
Entry Model	Factor Direction	Probability Weight
LC-1 - H1 OB is fractal	No	1.8969
LC-1 - Wicked the LID	No	1.5532
LC-1 - LID with FVG	Yes	1.1503
LC-1 - No imbalance while mitigation	No	1.7165
LC-1 - No other LIDs	Yes	1.4051
M15 - Target Liq LRLQ	Yes	1.5284
	25.01	47.77
```
I have assumed no for the entry factors that have not yet been formed.  I’ll wait for those to form and then change the factors to yes.  So in this current state, even if any one of the factors turn positive, then the trade probability would be above threshold and I can look for sells. 
![image.png](504/image%205.png)
![image.png](504/image%206.png)
Waited for the price to take out the BSLQ, but the price pushed down in my favour without me getting tagged in.  
## Post Session Notes
I missed a trade today.  The catch here is there was a chance of me entering the trade.  But the FOL kicked in and I wanted the price to push a bit higher as I spotted another BSLQ which the price might grab before pushing down.  I was sure about this as the price has swept some FVG liquidity and in the past we have seen that the price after sweeping the FVGs used to liquidate my stops before pushing down.  So that instinct automatically kicked in and actually I did not hesitate the take the trade completely but I was hesitant to take the trade without the price taking out the BSLQ.  If the price had taken that liquidity I would have been more confident that the price might push down atleast to take the M15 LRLQ which I marked during the pre session analysis.  I set an passive alert on the BSLQ, waiting for the price to liquidate that and then I can enter but since the price did not reach the liquidity point, the alert never went off.  Thus no trades for me today. 
Also the first entry model that is LC-2A actually completed.   That is price made a bearish fake break and then took the BSLQ at 11:30 am.  Then during NY open, the price pushed up again and took the liquidity candle.  So naturally I expected the price to push even higher. 
Emotions and thoughts:
- I do feel for the missed trade but at the same time I knew that I followed the rules and it was my instinct from the past results that did not allow me to take the trade and wanted me to wait for more confluences. 
- And yeah ofcourse, I am in a dry run without trades for a week.  So missing out a quick winner like this do hurt sometimes.

<!-- synced: 2026-06-01T17:42:00.000Z -->
