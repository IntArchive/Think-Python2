import string
def printdec(strin):
	strin = strin.lower()
	for lett in strin:
		if lett not in string.ascii_lowercase:
			strin = strin.replace(lett,"")
	t = dict(enumerate(tuple(strin)))
	sv = dict()
	reverse_sv = dict()
	b = list()
	for i in t:
		if t[i] not in sv:
			sv[t[i]] = 1
		else:
			sv[t[i]] = sv[t[i]] + 1
	for j in sv:
		if sv[j] not in reverse_sv:
			reverse_sv[sv[j]] = [j];
		else:
			reverse_sv[sv[j]].append(j)
	for k in reverse_sv:
		b.append((k, reverse_sv[k]))
	for l in sorted(b,reverse = True):
		print(l)
	return None
def main():
	printdec("WASHINGTON — After decades of getting schooled in information warfare by President Vladimir V. Putin of Russia, the United States is trying to beat the master at his own game.In recent weeks, the Biden administration has detailed the movement of Russian special operation forces to Ukraine’s borders, exposed a Russian plan to create a video of a faked atrocity as a pretext for an invasion, outlined Moscow’s war plans, warned that an invasion would result in possibly thousands of deaths and hinted that Russian officers had doubts about Mr. Putin. Then, on Friday, Jake Sullivan, President Biden’s national security adviser, told reporters at the White House that the United States was seeing signs of Russian escalation and that there was a “credible prospect” of immediate military action. Other officials said the announcement was prompted by new intelligence that signaled an invasion could begin as soon as Wednesday. All told, the extraordinary series of disclosures — unfolding almost as quickly as information is collected and assessed — has amounted to one of the most aggressive releases of intelligence by the United States since the Cuban missile crisis, current and former officials say. It is an unusual gambit, in part because Mr. Biden has repeatedly made clear he has no intention of sending U.S. troops to defend Ukraine. In effect, the administration is warning the world of an urgent threat, not to make the case for a war but to try to prevent one. The hope is that disclosing Mr. Putin’s plans will disrupt them, perhaps delaying an invasion and buying more time for diplomacy, or even giving Mr. Putin a chance to reconsider the political, economic and human costs of an invasion. At the same time, Biden administration officials said they had a narrower and more realistic goal: They want to make it more difficult for Mr. Putin to justify an invasion with lies, undercutting his standing on the global stage and building support for a tougher response. Intelligence agencies, prodded by the White House, have declassified information, which in turn has been briefed to Congress, shared with reporters and discussed by Pentagon and State Department spokesmen.")
if __name__ == '__main__':
	main()

