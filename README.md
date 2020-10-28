# Using logic to analyse the data

Writing a sentence such as:

_N measurements of this quantity were obtained.  The lowest value obtained was L, while the highest value was U._

Is a more useful way of summarising the data than simply calculating the mean.  Another researcher performing similar experiments can check their work by determining if their results fall into the same range as ours.  If a lot of the results they have obtained do not fall within the range of values we obtained it suggests that there is some marked difference between the experiments we have reported on and the experiments they are performing.  This sort of comparison would have been impossible if we had only reported the mean.

Whenever we compute a summary statistic, however, some of the information contained in the original data is lost.  For example, when we report simply the lowest and highest result we obtained in our experiments we lose all the information about how the other data points are spread across this range.  If only the range of data values is known we have no way of knowing,  for instance, if one experiment produced a result that was considerably larger than the results obtained in all the other experiments.

We can report on how the data is spread across the real number line by using what we have learned about writing Python programs that contain logic.  To complete this task I would thus like you to complete the four functions shown on the right:

1. `numberLessThan` - should return the number of data points that are less than or equal to `a`  
2. `fractionMoreThan` - should return the fraction of data points that are more than or equal to `a`
3. `percentageBetween` - should return the percentage of data points that are between `a` and `b`, where `a`<`b`
4. `percentageOutside` - should return the percentage of data points that are not between `a` and `b`, where `a`<`b`
