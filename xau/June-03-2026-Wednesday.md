# 506

Date: June 3, 2026
Day: WEDNESDAY
ATTENDANCE: PRESENT
Pair: XAU
DAY RESULT: Win
HTF Strength: 52.86%
Narrative Achieved: In Progress

## Pre Session Notes:
![image.png](506/image.png)
![image.png](506/image%201.png)
![image.png](506/image%202.png)
![image.png](506/image%203.png)
## Session Updates
```javascript
Confluence Factor			Factor Support	Weight
Daily Swing 			Yes	1.0237
Daily Internal 			Yes	0.5615
Daily Fractal			No	1.0242
Daily in Internal OTE			Yes	0.6226
	Previous Candle		No	0.6391
Daily Mitigation OB - Has Inducement			Yes	1.0542
Daily Mitigation OB - Caused Imbalance			Yes	1.1649
Daily Mitigation OB - Caused Displacement			No	1.4231
Daily Mitigation OB - Flipzone			Yes	1.4232
	Structural - Fractal		Yes	0.9337
Daily Liquidity Sweep - Equals			Yes	1.0474
Daily Liquidity Sweep - FVG			Yes	1.5166
	Structural - Internal		Yes	0.6534
4H Swing 			Yes	0.6204
4H Internal 			Yes	1.0236
4H Fractal			Yes	1.1315
4H Price in Swing OTE			Yes	0.3403
4H Price in Internal OTE			No	0.975
	FVG Liquidity		Yes	1.0781
	Previous Candle		Yes	1.1065
4H Mitigation OB - Has Inducement			No	1.1535
4H Mitigation OB - Caused Imbalance			No	0.9442
4H Mitigation OB - Caused Displacement			Yes	1.2743
4H Mitigation OB - Flip Zone			No	0.8543
4H Mitigation OB - Within daily OB			No	0.7361
4H Liquidity Target - FVG Liquidity			Yes	1.3418
H1 Swing 			Yes	1.0235
H1 Internal 			Yes	0.9262
H1 Fractal			Yes	1.1315
H1 Price in Swing OTE			No	0.7999
	Previous Candle		Yes	1.4096
H1 Mitigation OB - Has Inducement			Yes	0.7587
H1 Mitigation OB - Caused Imbalance			No	1.0239
H1 Mitigation OB - Caused Displacement			Yes	0.9266
H1 Mitigation OB - Flip Zone			Yes	0.7579
H1 Mitigation OB - Within 4H OB			No	0.8382
H1 Liquidity Sweep - PDH/PDL			No	1.1709
	Structural - Internal		Yes	1.0251
	P(t)		52.86	
```
```javascript
Entry Model	Factor Direction	Probability Weight
LC-1 - H1 OB is fractal	No	1.8969
LC-1 - Wicked the LID	No	1.5532
LC-1 - LID with FVG	Yes	1.1503
LC-1 - No imbalance while mitigation	No	1.7165
LC-1 - No other LIDs	No	1.4051
M15 - Target Liquidity	No	0.9348
	-8.26	44.52
```
The entry model factors which are marked no are not yet formed.  I am assuming it as now just for the instance.  Once the price reaches the liquidity point, then I can modify it.  There could be a trade if the following happened:
- LC wicked the M15 BSLQ
- LC wicked the second BSLQ so that No other LID would be positive
- M15 must form an equal lows or a engineer some SSLQ before pushing up and taking out the BSLQ.
If all the above three conditions satisfy then the total trade quality would be above threhsold (50%) and then I can look for sells. 
Assumptions Made during Analysis:
- For the daily mitigation OB, I took the fractal OB which the price is in and which is against our trade.  So the yes factors actually means no.  
- There is also an old demand which I did not take.  Actually I took it during my first round of analysis and saw that the bearish bias was only 49.5%.  So I tried with the recent daily fractal demand and the probability pushed up a liitle above the threshold.   - Could we call this a FOMO?   Here are the reasons why I took the recent daily fractal supply
	- It is recently formed
	- The old demand was already mitigated but it is not yet invalidated.  
![image.png](506/image%204.png)
![image.png](506/image%205.png)
Price did not mitigate the H1 supply it is moving down without mitigating it.  Now I realize that the H1 supply is partially mitigated earlier.  Thus considering the new H1 supply for analysis
```javascript
Confluence Factor			Factor Support	Weight
Daily Swing 			Yes	1.0237
Daily Internal 			Yes	0.5615
Daily Fractal			No	1.0242
Daily in Internal OTE			Yes	0.6226
	Previous Candle		No	0.6391
Daily Mitigation OB - Has Inducement			Yes	1.0542
Daily Mitigation OB - Caused Imbalance			Yes	1.1649
Daily Mitigation OB - Caused Displacement			No	1.4231
Daily Mitigation OB - Flipzone			Yes	1.4232
	Structural - Fractal		Yes	0.9337
Daily Liquidity Sweep - Equals			Yes	1.0474
Daily Liquidity Sweep - FVG			Yes	1.5166
	Structural - Internal		Yes	0.6534
4H Swing 			Yes	0.6204
4H Internal 			Yes	1.0236
4H Fractal			Yes	1.1315
4H Price in Swing OTE			Yes	0.3403
4H Price in Internal OTE			No	0.975
	FVG Liquidity		Yes	1.0781
	Previous Candle		Yes	1.1065
4H Mitigation OB - Has Inducement			No	1.1535
4H Mitigation OB - Caused Imbalance			No	0.9442
4H Mitigation OB - Caused Displacement			Yes	1.2743
4H Mitigation OB - Flip Zone			No	0.8543
4H Mitigation OB - Within daily OB			No	0.7361
4H Liquidity Target - FVG Liquidity			Yes	1.3418
H1 Swing 			Yes	1.0235
H1 Internal 			Yes	0.9262
H1 Fractal			Yes	1.1315
H1 Price in Swing OTE			No	0.7999
	Previous Candle		Yes	1.4096
H1 Mitigation OB - Has Inducement			Yes	0.7587
H1 Mitigation OB - Caused Imbalance			No	1.0239
H1 Mitigation OB - Caused Displacement			Yes	0.9266
H1 Mitigation OB - Flip Zone			Yes	0.7579
H1 Mitigation OB - Within 4H OB			No	0.8382
H1 Liquidity Sweep - PDH/PDL			No	1.1709
	Structural - Internal		Yes	1.0251
	P(t)		52.86	
```
```javascript
Entry Model	Factor Direction	Probability Weight
CE - IBos with body close	Yes	0.8382
CE - H1 OB is internal	Yes	1.2477
CE - Has imbalance	No	0.8363
CE - Has inducements	No	1.2478
CE - Swept Liquidity	Yes	1.3795
CE - No other LIDs	No	0.9728
M15 - Target Liquidity	Yes	0.9348
	41.03	51.02
```
Not the greatest of entry model, but still it is above the threshold.  Thus I am placing the trade. 
![image.png](506/image%206.png)
![image.png](506/image%207.png)
Price started moving in my direction after tagging me in.  Price now reached a M15 demand zone and it is reacting off it.  There is urge to bring the trade to BE but there is no BE plan in my rules.  So if I do that, that would would be a FOL emotion.  Currently controlling my emotion and staying away from charts. 
![image.png](506/image%208.png)
![image.png](506/image%209.png)
![image.png](506/image%2010.png)
Price hit the TP.  That’s 2.7R for the day.  Closing off for today. 
## Post Session Notes
Coming to the session the plan was to look for sells and target the 4H FVG liquidity.  The numbers were good. There was slight feeling of FOMO today for which I had logical answers but still categorized them as FOMO as I need to review them over time to make sure that those are actually FOMO’s are technical intuition.  But overall the trade probability changed very minutely because of that assumption.  The entry model was also good if not there would have been no trades today.  
I kept the trade and while the trade moved half way through insticts kicked in and asked me to BE and secure the profits.  Also I saw an M15 demand from which the price made slight reaction.  I somehow controlled myself and forced myself with office job and kept myself away from charts.  Eventually the price flipped the M15 demand zone and then reached my target.  
Even if I had the SL at BE, it would not have been mattere as the price reached the BE point only after reaching 4.15R. 
Thus a good trade today.

<!-- synced: 2026-06-03T17:40:00.000Z -->
