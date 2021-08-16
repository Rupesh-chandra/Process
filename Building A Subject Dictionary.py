#!/usr/bin/env python
# coding: utf-8

# In[37]:


import time
import string
from operator import itemgetter, attrgetter

SUBJECT_FILENAME = "my_subjects.txt"
SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1


# In[38]:



#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".
    
    returns: dictionary mapping subject name to (value, work)
    """
    result = {}
    inputFile = open(filename)
    
    for line in inputFile:
        line = line.strip()
        line_as_list = line.split(',')
        result[line_as_list[0]] = (int(line_as_list[-2]),int(line_as_list[-1])) 
    return result
            
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2


# In[48]:


#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.
    
    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """    
    # TODO...
    #
    # Build function that sorts based on comparator returns list of subject names sorted by comparator criteria.
    #
    def sort(l, comparator) :
        """
        Sorts the list of subjects' names in descendig order
        acording to the comparator.
        """
        # print "l, comparator type:", type(l), type(comparator)
        # print 
        
        for i in range(1, len(l)) :
            value = l[i]
            j = i - 1
            done = False
            # print 'i, value, j', i, value, j
            # print
            while not done:
                # print "subjects[value], subjects[l[j]] type:", type(subjects[value]), type(subjects[l[j]])
                # print
                if comparator(subjects[value], subjects[l[j]]):
                    l[j+1] = l[j]
                    j -= 1
                    if j < 0 :
                        done = True
                else :
                    done = True
            l[j+1] = value
    #
    # Pick classes from top of sorted list until maxWork is reached
    #
    schedule_list = list(subjects.keys())
    #print 'schedule_list unsorted: ', schedule_list
    #print
    sort(schedule_list, comparator)
    # print 'schedule_list sorted: ', schedule_list
    #     print
    recommended_schedule = {}
    courseLoad = 0
    done = False
    for course in schedule_list:
        if subjects[course][1] <= maxWork - courseLoad:
            recommended_schedule[course] = subjects[course]
            courseLoad += subjects[course][1]
    return recommended_schedule


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.
        
    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work) 
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue =             bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects


counter = 0

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue, subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#

def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    trial_work = [15]
    total_times = {}
    for each in trial_work:
        start_time = time.time()
        print (bruteForceAdvisor(subjects,each))
        end_time = time.time()
        total_times[each] = round(end_time - start_time, 2)
    print (total_times)


# In[49]:



# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
# Th brute force function is very slow for even moderately large course loads.
      #For a maxLoad of  2: 0.01 seconds
                           # 4: 0.22
                           # 6: 1.76
                           # 7: 3.70
                           # 8: 11.42
                           # 9: 27.57
                           # 10: 122.58
                           # 11: 354.55
                           # 12: 778.29
                           # 13: 1714.95
                           # 14: 2907.09
                           # 14: 2850.40
       # Unreasonable depends on a multiple  factors, including the importance of the results and the quality of the results of a faster, less optimal function.  In this case the greedy function probably produces results that nearly as good as the results of the brute force method.
   #  Considering MIT costs ~$200k in tuition and room and board.  Perhaps a few minutes to optimize a semester course load is worth it. 
   



# In[50]:


#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.
    
    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    
    These are the results for running this full catalog:
    {8: 0.02, 10: 0.01, 45: 0.080000000000000002, 15: 0.02, 120: 0.23000000000000001, 90: 0.23000000000000001, 60: 0.11, 30: 0.050000000000000003}
        
    """
    # TODO...
    
    rec_dict = {}
    m = {}
        
    #   Build the work and value lists.
    work_list = []
    value_list = []
    key_list = []
    for each in subjects:
        work_list.append(subjects[each][1])
        value_list.append(subjects[each][0])
        key_list.append(each)
    
    # Build optimal list of courses to take.
    value, rec_list = dp_decision_tree(work_list,value_list,len(work_list)-1,maxWork,m)
    
    #   Build dictionary from list.
    for each in rec_list:
        rec_dict[key_list[each]] = (value_list[each],work_list[each])
    return rec_dict

def dp_decision_tree(w,v,i,aW,m):
    """
    Creates a course schedule that is optimized the maximum value.
    """
    
    ## check if value is already in the dictionary
    try: return m[(i,aW)]
    except KeyError:
        ##  Leaf/Bottom of the tree case decision
        if i == 0:
            if w[i] < aW:
                m[(i,aW)] = v[i], [i]
                return v[i],[i]
            else:
                m[(i,aW)] = 0, []
                return 0,[]
    
    ## Calculate with and without i branches
    without_i, course_list = dp_decision_tree(w,v,i-1,aW,m)
    if w[i] > aW:
        m[(i,aW)] = without_i, course_list
        return without_i, course_list
    else:
        with_i, course_list_temp = dp_decision_tree(w, v, i-1, aW - w[i], m)
        with_i += v[i]
    
    ## Take the branch with the higher value
    if with_i > without_i:
        i_value = with_i
        course_list = [i] + course_list_temp
    else:
        i_value = without_i
    
    ## Add this value calculation to the memo
    m[(i,aW)] = i_value, course_list
    return i_value, course_list
    


# In[51]:



#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    
    Prints total schedule, recommended schedule, time to complete each trial.
    """
    # TODO...
    trial_work = [8,10,15,30,45,60,90,120]
    total_times = {}
    for each in trial_work:
        print ("Trial for max workload of %i." % each)
        start_time = time.time()
        recommendation = dpAdvisor(subjects, each)
        end_time = time.time()
        total_times[each] = round(end_time - start_time, 2)
        printSubjects(recommendation)
    print (total_times)
    return
    
    

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

subjects = loadSubjects(SUBJECT_FILENAME)
dpTime()


# In[52]:


print(subjects)
#print "Course Catalog"
print(loadSubjects(SUBJECT_FILENAME))


# In[64]:


print ('greedy(cmpValue):')
printSubjects(greedyAdvisor(subjects, 15, cmpValue))
# 
print ('\ngreedy(cmpWork):')
printSubjects(greedyAdvisor(subjects, 15, cmpWork))
# 


# In[65]:


print('\ngreedy(cmpRatio)')
printSubjects(greedyAdvisor(subjects, 15, cmpRatio))


# In[69]:


printSubjects(dpAdvisor(subjects, 15))


# In[ ]:




