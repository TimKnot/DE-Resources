# Use keyboard shortcuts to speed up these common tasks
# No mouse required! Put it on the floor or something!
# Alt+↓/↑ (⌥↓/↑)
# Place your cursor on a line and use the above shortcut. The line will move
# Sort these lines into alphabetical order

# Foxtrot
# Charlie
# Bravo
# Delta
# Echo
# Alfa

# Create a selection that spans multiple lines. Use the previous shortcut. The whole set of lines moves.
# 1. Move the second function so that it is above the first function
# 2. Then swap the return statements so iGoDown returns "down" and iGoUp returns "up"

def iGoDown():
  print ("Better hope I end up at the bottom!")
  return "up"

def iGoUp():
	print ("Better hope I end up at the top!")
	return "down"

# Ctrl+] (⌘]) and Ctrl+[ (⌘[)
# Place your cursor on a line. Use one of the above shortcuts. It moves left or right
# Fix the indentation in this set of nested ifs

if (True):
print ("how did I get here?")
else:
print ("This was entirely expected")

# Create a selection that spans multiple lines. Use the previous shortcut. The whole set of lines moves.
# Indent the whole for-loop one level to the right

def maybeLoop(doALoop):
	if(doALoop):
	for i in range(0,10):
		console.log("Look at me loop " + i)

# Ctrl+Shift+K (⇧⌘K)
# The above shortcut deletes the line your cursor is on
# Delete all the comments in the following code

# Look at my horse
def horse():
	# My horse is amazing
	amazing = True
	# Give it a lick
	flavour = lick()
	if (flavour == "raisins"):
		# It tastes just like raisins
		console.log("yum")

# Create a selection that spans multiple lines. Use the previous shortcut. The whole set of lines is deleted.
# There is an infinite loop in this function. Delete it in a single stroke

def youDoComputersCanYouFixMyPrinter():
	print ("Have you tried turning it off and on again")
	while (True):
		print ("Can't talk now. Look how busy I am")
	print ("I can help you with your broken printer now")
}

# ================
# MULTIPLE CURSORS
# FEEL THE POWER
# ================

# Win         Linux        Mac
# Ctrl+Alt+↓  Shift+Alt+↓  ⌥⌘↓
# The above shortcut creates a new cursor below your current one. Any subsequent key-press is accepted by all cursors
# The time stamps are no longer needed from the start of these logs. Remove them all with as few key strokes as possible
# (hint: you can use shift+home to quickly select to the start of the line)

"""
Apr 11 10:32:22 router1 mgd[3606]: UI_DBASE_LOGOUT_EVENT: User 'barbara' exiting configuration mode
Apr 11 11:36:15 router1 mgd[3606]: UI_COMMIT: User 'root' performed commit: no comment
Apr 11 11:46:37 router1 mib2d[2905]: SNMP_TRAP_LINK_DOWN: ifIndex 82, ifAdminStatus up(1), ifOperStatus down(2), ifName at - 1 / 0 / 0
Feb 22 20:35:07 router1 snmpd[359]: SNMPD_THROTTLE_QUEUE_DRAINED: trap_throttle_timer_handler: cleared all throttled traps
Feb 23 07:34:56 router1 snmpd[359]: SNMPD_TRAP_WARM_START: trap_generate_warm: SNMP trap: warm start
Feb 23 07:38:19 router1 snmpd[359]: SNMPD_TRAP_COLD_START: trap_generate_cold: SNMP trap: cold start
"""

# Change all the 500s to 100s
"""
-webkit-transition: all 500ms linear;
-moz-transition:    all 500ms linear;
-o-transition:      all 500ms linear;
transition:         all 500ms linear;
"""

# Alter the following code to read [1, 2, 3, 4] with the fewest key strokes possible

[
	1,
	2,
	3,
	4
]

# Add an exclamation mark to the end of all of these strings
# (hint: remember Home and End)
"Ra ra Rasputin"
"Lover of the Russian queen"
"There was a cat that really was gone"
"Ra ra Rasputin"
"Russia's greatest love machine"
"It was a shame how he carried on"

# I have copied and pasted these lines carelessly.
# The numbers passed to getEnd should always be the same as those passed to getStart
# Fix all lines at the same time with multiple cursors
# (hint, use Copy and Paste (Ctrl+C, Ctrl+V))

list[0] = getStart(0) + "alpha" + getEnd(0)
list[1] = getStart(1) + "beta" + getEnd(0)
list[2] = getStart(2) + "gamma" + getEnd(0)
list[3] = getStart(3) + "delta" + getEnd(0)
list[4] = getStart(4) + "epsilon" + getEnd(0)

# Each of these lines should be once sentence. They have got messed up somehow. Fix it
# (hint, ctrl+shift+right selects a whole word)

"""
The caterpillar ate through one nice leaf, and after that he felt 
better.Now he wasn't hungry anymore--and he wasn't a little caterpillar 
anymore.He was a big fat 
caterpillar.He built a small house, called a cocoon around 
himself.
"""

# In the command palette you will find a command for 'transform to uppercase'
# Using multiple cursors, capitalize the first letter of each of these lines:

"""
let me not to the marriage of true minds
admit impediments. Love is not love
which alters when it alteration finds,
or bends with the remover to remove.
o no! it is an ever-fixed mark
that looks on tempests and is never shaken;
it is the star to every wand'ring bark,
whose worth's unknown, although his height be taken.
"""

# Ctrl+D (⌘D)
# Make a selection. Use the above shortcut. The next occurrence of that selection is also selected
# Keep pressing it and you can select many occurrences
# Delete the comments in this code by pressing Ctrl+Shift+K only once

# Look at my horse
def horse():
	# My horse is amazing
	amazing = True
	# Give it a lick
	flavour = lick()
	if (flavour === "raisins"):
		# It tastes just like raisins
		print("yum")

# Make nato1 look exactly like nato2 using multiple cursors

const nato1 = { a: "alpha", b: "bravo", c: "charlie", d: "echo" }

nato2 = {
	a: "alpha",
	b: "bravo",
	c: "charlie",
	d: "echo"
}
