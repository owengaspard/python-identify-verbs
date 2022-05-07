import nltk

greatWar = """ World War I or The First World War, often abbreviated as WWI or WW1, began on the 28th of July, 1914 and ended on the 11th of November, 1918. Referred to by contemporaries as the "Great War", belligerents included much of Europe, Russia, the United States and Turkey, with fighting also expanding into the Middle East, Africa and parts of Asia. One of the deadliest conflicts in history, an estimated 9 million were killed in combat, while over 5 million civilians died from occupation, bombardment, hunger or disease.[4] Millions of additional deaths resulted from genocides within the Ottoman Empire and the 1918 Spanish flu pandemic, which was exacerbated by the movement of combatants during the war.

By 1914, the European great powers were divided into the Triple Entente of France, Russia, and Britain, and the Triple Alliance, Germany, Austria-Hungary, and Italy. Tensions in the Balkans came to a head on 28 June 1914 following the assassination of Archduke Franz Ferdinand, the Austro-Hungarian heir, by Gavrilo Princip, a Bosnian Serb. Austria-Hungary blamed Serbia and led to the July Crisis, an unsuccessful attempt to avoid conflict through diplomacy. When Austria-Hungary declared war on Serbia on 28 July, Russia came to its defence and by 4 August the system of alliances drew in Germany, France and Britain, along with their respective empires. In November, the Ottoman Empire, Germany and Austria formed the Central Powers, while in April 1915, Italy joined Britain, France, Russia and Serbia as the Allied Powers.

Facing a war on two fronts, German strategy in 1914 was to first defeat France, then shift its forces to the East and knock out Russia, commonly known as the Schlieffen Plan.[7] Their advance into France failed and by the end of 1914 the two sides faced each other along the Western Front, a continuous series of trench lines stretching from the Channel to Switzerland that changed little until 1917. By contrast, the Eastern Front was far more fluid, with Austria-Hungary and Russia gaining, then losing large swathes of territory. Other significant theatres included the Middle East, the Alpine Front and the Balkans, bringing Bulgaria, Romania and Greece into the war.

Shortages caused by the Allied naval blockade led Germany to initiate unrestricted submarine warfare in early 1917, bringing the previously neutral United States into the war on 6 April 1917. In Russia, the Bolsheviks seized power in the 1917 October Revolution and made peace in the March 1918 Treaty of Brest-Litovsk, freeing up large numbers of German troops. By transferring these to the Western Front, the German General Staff hoped to win a decisive victory before American reinforcements could impact the war, and launched the March 1918 German spring offensive. Despite initial success, it was soon halted by heavy casualties and ferocious defence; in August, the Allies launched the Hundred Days Offensive and although the German army continued to fight hard, it could no longer halt their advance.

Towards the end of 1918, the Central Powers began to collapse; Bulgaria signed an Armistice on 29 September, followed by the Ottomans on 31 October, then Austria-Hungary on 3 November. Isolated, facing revolution at home and an army on the verge of mutiny, Kaiser Wilhelm abdicated on 9 November and the new German government signed the Armistice of 11 November 1918, bringing the fighting to a close. The 1919 Paris Peace Conference imposed various settlements on the defeated powers, the best known being the Treaty of Versailles. The dissolution of the Russian, German, Ottoman and Austro-Hungarian empires led to numerous uprisings and the creation of independent states, including Poland, Czechoslovakia and Yugoslavia. For reasons that are still debated, failure to manage the instability that resulted from this upheaval during the interwar period ended with the outbreak of World War II in 1939.
"""
greatWar

#Taken from https://en.wikipedia.org/wiki/World_War_I

tokens = nltk.word_tokenize(greatWar)
tagged = nltk.pos_tag(tokens)

entities = nltk.chunk.ne_chunk(tagged)

VERBS = []
for s in entities:
  if len(s) > 1:
    if s[1] == "VBD" or s[1] == "VB" or s[1] == "VBG" or s[1] == "VBN" or s[1] == "VBP" or s[1] == "VBZ":
      VERBS.append(s[0].lower())

verbs = [v for v in sorted(list(set(VERBS)))]
print(verbs)