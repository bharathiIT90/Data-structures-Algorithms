# /********************************************************************** 
#  *                                                     *
#  *                                                                    *
#  *  Prompt: Given a set S, return the power set P(S), which is        *
#  *          a set of all subsets of S.                                *
#  *                                                                    *
#  *  Input:  A String                                                  *
#  *  Output: An Array with the power set of the input string           *
#  *                                                                    *
#  *  Example: S = "abc", P(S) = ['', 'a', 'b','c','ab','ac','bc','abc']*                                                               *
#  *                                                                    *
#  *  Note: There should not be any duplicates in the power set         *
#  *        ('ab' and 'ba' are considered the same), and it will always *
#  *        begin with an empty string ('')                             *
#  *                                                                    *
#  **********************************************************************/

def powerSet(input):
    result = []

    def traverse(build, depth):
        #print "for", depth, "build is", build
        if(depth==len(input)):    
           result.append(build)
           return

        traverse(build,depth+1)
        traverse(build + input[depth],depth+1)

    traverse('',0)
    return result


p = powerSet('abc')
print sorted(list(set([''.join(sorted(i)) for i in p])))
