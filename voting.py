import random
def campaining(voters):
    list_pos = [] #list for party A
    list_neg = [] #list for party B
    list_neu = [] #list for neutral Party
    pos = 0
    neg = 0
    neu = 0
    for influencer in voters:
        friends = influencer['connected']
        #print(friends)
        for j in friends:
            v_en=float(voters[j]['endurance'])
            in_en=float(influencer['endurance'])
            in_in=float(influencer['influence'])
	        
            if v_en>0 and in_en>0:
		    #if the voter and influencer belongs to the same party A
                voters[j]['endurance'] = v_en+(in_in*random.uniform(0, 0.2))
            elif v_en<0 and in_en<0:
	    	#if the voter and influencer belongs to the same party B
                voters[j]['endurance'] = v_en-(in_in*random.uniform(0, 0.2))
            elif v_en >0 and in_en<0:
	    	#if voter belongs to A and influencer in B
               	voters[j]['endurance'] = v_en-(in_in*random.uniform(5, 10))
            elif v_en<0 and in_en>0:
	    	#if voter belongs to B and influencer in A
               	voters[j]['endurance'] = v_en+(in_in*random.uniform(5, 10))
            elif v_en==0 and in_en>0:
                voters[j]['endurance'] = in_in
            elif v_en==0 and in_en<0:
                voters[j]['endurance'] = -1 * in_in
            
        #    print(j, voters[j]['endurance'])
        #print('\n')
        pos = 0
        neg = 0
        neu = 0
        for j in range(len(voters)):
            if float(voters[j]['endurance'])>0:
                pos += 1
            elif float(voters[j]['endurance'])<0:
                neg += 1
            else:
                neu += 1
        list_pos.append(pos)
        list_neg.append(neg)
        list_neu.append(neu)

    return (voters, list_pos,
            list_neg,
            list_neu)
