class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def sort_key(s):
            if s[-1].isdigit():
                return (1, )
            else:
                a, b = s.split(" ", 1)
                return (0, b, a)
        logs.sort(key = sort_key)
        return logs