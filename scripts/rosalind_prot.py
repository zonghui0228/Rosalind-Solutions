Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fp=open('C:\\Users\\sony\\Desktop\\rosalind_prot.txt','r')
>>> str=fp.read()
>>> i=0
>>> prot=''
>>> a=''
>>> while (i<len(str)-2):
	if str[i:i+3]=='AUG':
		a+='M'
	elif str[i:i+3]=='GCU':
		a+='A'
	elif str[i:i+3]=='GCC':
		a+='A'
	elif str[i:i+3]=='GCA':
		a+='A'
	elif str[i:i+3]=='GCG':
		a+='A'
	elif str[i:i+3]=='UGU':
		a+='C'
	elif str[i:i+3]=='UGC':
		a+='C'
	elif str[i:i+3]=='GAU':
		a+='D'
	elif str[i:i+3]=='GAC':
		a+='D'
	elif str[i:i+3]=='GAA':
		a+='E'
	elif str[i:i+3]=='GAG':
		a+='E'
	elif str[i:i+3]=='UUU':
		a+='F'
	elif str[i:i+3]=='UUC':
		a+='F'
	elif str[i:i+3]=='GGU':
		a+='G'
	elif str[i:i+3]=='GGC':
		a+='G'
	elif str[i:i+3]=='GGA':
		a+='G'
	elif str[i:i+3]=='GGG':
		a+='G'
	elif str[i:i+3]=='CAU':
		a+='H'
	elif str[i:i+3]=='AUU':
		a+='I'
	elif str[i:i+3]=='AUC':
		a+='I'
	elif str[i:i+3]=='AUA':
		a+='I'
	elif str[i:i+3]=='AGA':
		a+='R'
	elif str[i:i+3]=='AGG':
		a+='R'
	elif str[i:i+3]=='AAA':
		a+='K'
	elif str[i:i+3]=='AAG':
		a+='K'
	elif str[i:i+3]=='CUU':
		a+='L'
	elif str[i:i+3]=='CUC':
		a+='L'
	elif str[i:i+3]=='CUA':
		a+='L'
	elif str[i:i+3]=='CUG':
		a+='L'
	elif str[i:i+3]=='AUG':
		a+='M'
	elif str[i:i+3]=='AAU':
		a+='N'
	elif str[i:i+3]=='AAC':
		a+='N'
	elif str[i:i+3]=='CCA':
		a+='P'
	elif str[i:i+3]=='CCG':
		a+='P'
	elif str[i:i+3]=='CCU':
		a+='P'
	elif str[i:i+3]=='CCC':
		a+='P'
	elif str[i:i+3]=='CAA':
		a+='Q'
	elif str[i:i+3]=='CAG':
		a+='Q'
	elif str[i:i+3]=='CGU':
		a+='R'
	elif str[i:i+3]=='CGC':
		a+='R'
	elif str[i:i+3]=='CGA':
		a+='R'
	elif str[i:i+3]=='CGG':
		a+='R'
	elif str[i:i+3]=='UCU':
		a+='S'
	elif str[i:i+3]=='UCC':
		a+='S'
	elif str[i:i+3]=='UCA':
		a+='S'
	elif str[i:i+3]=='UCG':
		a+='S'
	elif str[i:i+3]=='AGU':
		a+='S'
	elif str[i:i+3]=='AGC':
		a+='S'
	elif str[i:i+3]=='ACU':
		a+='T'
	elif str[i:i+3]=='ACC':
		a+='T'
	elif str[i:i+3]=='ACA':
		a+='T'
	elif str[i:i+3]=='ACG':
		a+='T'
	elif str[i:i+3]=='UUA':
		a+='L'
	elif str[i:i+3]=='UUG':
		a+='L'
	elif str[i:i+3]=='GUU':
		a+='V'
	elif str[i:i+3]=='GUC':
		a+='V'
	elif str[i:i+3]=='UGG':
		a+='W'
	elif str[i:i+3]=='GUA':
		a+='V'
	elif str[i:i+3]=='GUG':
		a+='V'
	elif str[i:i+3]=='UAU':
		a+='Y'
	elif str[i:i+3]=='UAC':
		a+='Y'
	elif str[i:i+3]=='CAC':
		a+='H'
	elif str[i:i+3]=='UGA':
		a+='';

	i+=3;

	
>>> a
'MAHASPRFYAQLQSGIVSQYASNVSGFPRSVGGIGDRRSLLRWPAWAGETMNAENGGIPANPRVANPYGCLGRTRGAYCTPCIRVTHKHTPQSLASPLASCAQPRLLSLGKRSRNVLYPTQSAASLMRYCFAEPKNISTATTSASGYRNPEYRGSTDLLKRLTRCHMPGRRLDSSPYPHSHHSQERKCFDTEYAKRCDLTYLPKGGPIVWRPLLTPRGLTAASQPDNTRECYTHGQKRCIDEYSRHLRRCATGAYLCPPYLAVADSVQFDQTSLGSLLFNCTTHRQCGDLSRTKVPGKRISLAQCHRLDLKSSPFYGARTPRQNQDFRLWTAVITIGHRSSISAHSSTIRRSGPRERMDTSNPNRPNLQGPVQPSPSSCKGVLPGAQELHFLKPLFCTFEIQLLLVGAAWDGWIEKRHGVIILCDLGEFGKVLLSGVQRKRVARTRIRVLVFAMYRFSRRHLVCLGTYSRCILWSSTPQSWTLLTQCELKMKSETALRILSLFLNSGTTIPEHYFSRFCQTLHASYPTDPTPYSPSQALRRVLVGSSREISVHSRYSGDRRHIRRTSRIPGLVEWVERAYANDPILSNLPDVDSPGNLQDSHETFCESPSPYADEAIVLVFLSPTFKLHLISEHVVHALLNGTLNQPIGIFSHGVSEIPSTQSAPLKVIRTDVPYLKAAPFYSPTNFDRTGKRGLTLPCVAAVAQCIVQPCRLCGTGPQTTVSRPGKILTSHRCRIWYDFALLLTVCHIGNGRAISRTVKLKLSDLELAGITPPRFLLFRLLLVYSGPLRVPVSPPFLALHVERAVLSDCQYPKVTSASRWPLQDQTRLDDTCPILKRRLRIANSPTNATRSFPVRCRFRPIFRPGVVLPFSLGPDRHSPNGTRRHTLNDRQWESFTTYTLWLGNARTHQQSGAWMTVPNPDCFPCNLRRFWSAGSLHCNDTSNDLARRVVQITVTYMTVRHKSGPIWSYKRLDQLSGFQCFSISDYPQKSKWTVTLSDWLSQVGVNRRDAPAYTLRLKSCIPPKRGAAFSSRRYILRAPGPDTTAADHSLTGKPFLFFFNHVGTQAVRFRGWLARAVQYPATVYPRGNDRLARVCSDRSASQVCDPGEGTDLPVLYLTGSAARASRVKPRGRAPPLHISRYWDHRSYAFRRLRYYVGDVDLIHRTYGGVKCPGSGRARDVRCHGQMKWNILAQYEEMHRCTVLESACSDAQTAPDSSLGTMPWLKVTCTEFQLHNGEERMGASPILWRGSTVPVVGHLQKAPFGYGLSISGQYCHSGQGICNTPTVHHTTMTACCHIPNSGEYQLQGLARVAPMFLFGTHWRQQWERIPLIGNEKYGPNTKSTYTHLYSRKAILPCTFLGVRPHRLRKCTMVSGCFGDGPPIGIGSNREILCQVATRTTCRELTCSCTPWGLTLAPFSAGCGDSGDIIINEYTVRSKASIVVRLLSKVADACSTTRKESNLLDRWVVHLYGICARSGHVVRKLAMPAPANSRSIATQMIVLPITIRNCGEPEPATDGYTPQAAFIIQRQKNSGDSAYALTEGGTLPSDSTLYPLRLFYGYLSSTRRGIWLQVSTNVHSSRLISEAGRKVPPQIYWQVNNVYTHCHTICLDIQLTRCQFSRAMRVKVHLTVGALNEPAVICGLSAWEDDPQMEALRTHTGGGCPRWWLATAVYPYFEILRCIRLTVNLPTVVLSISITIRYEEVVPITRMGKCPMNQFYMLGSSHTNALRTPCITKVCGPTRVRVQVSGYSTCTSLVHDMGGRSGDRHPVRKPPVDYPLDKRDLPPCLTRNIVDSCRCERRAAYTTDQCPCGARQQTLLLSSNRLSASTREDLGQSTRSTCYERGPSLACAVDLGSNAVYYLIMTDNGWLGQLTAGFMQSALDRAALLKWRLIMQDFRLLRLSTRSFHMSARIKVSLSIYFRIPRRKRICTLRLIPSRVMSLSGPPLYHQAHCETSELQKGRASSLGRYWDSSASSVVQLHEERPPQQAGQLRQLEINFTPYCYAQANAIREPAESTVVSWQNPLWEAFAGPILLFRPRGTTHFAVWILAWAPYLTKVGSPFTYQLFRLANTLTATERAVVGNPVRTTADKMDLSTRQPSSLEGTKAGVVKPRVVFGASLKCSDDVSFRRDYFYVSDCVPLECLGRVSYTATARSGAKCAYKRFVSMGVWVKRRRTQVKSVRSQAASYVKEACLETLPTRLSDLHMPAAPLSSVLRCYAYLLLTSWLLRKSMRTVSRTRSEALSALSEAFLSALTNGPRGGYITSGVIRRAQSPGMRRQDENVSGETRHSKSEVEMWNNCRAQTAKKITDSGGNRANEGVGYGCPGHHCVNPSRAIPASRREKCETNNAWWVQLVLRMGTAAVLWAQIPCTVPGEEIGATEGVSPSGNQSPETPNIYRLLSGSSDHAYSCGSDTASCLGVIGHRTKSGPYRRFLKTFSILLVSNSVTRHFIHSSTYLQPGIRPANGAKSRTHESLCCTTATIGEWDSLHPRNNTGVWLQVQPPAQPGTVIRRQFHSETLGCKVVLATPTCSFGSSLCNMIHCLWGRAKYNKSNLRITSSATISGATRYLIPEQALCLPSRIKDAVRRVLGSTTVPNTERTTSRLLPSNFCRMLYIHTLKSCTIGVPKRKQLAWITDPSVDLLVSPVRGWMTRYAISHSMLLNQRVWMATSPADCTTSSMIGRASHTLLRVFNQSRKLIATLILTPSCGNPVYPGREPDNFGYYGGVVIYGFIPREASWPLI'
>>> 
