class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you
        :param area:
        :return:
        """
        import math
        mid = int(math.sqrt(area))

        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), mid]
            mid -= 1
