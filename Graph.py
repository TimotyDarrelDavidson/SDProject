class VideoRecommendationGraph:
    def __init__(self, videos):
        # Initialize the class with a list of videos.
        # Each video is represented by a dictionary containing 'title' and 'tags' (set of strings).
        self.videos = videos
        self.recommendation_graph = {}

    def findWeight(self, tags1, tags2):
        """Calculate Jaccard similarity between two sets of tags."""
        intersection = len(tags1 & tags2)
        union = len(tags1 | tags2)
        return intersection / union if union != 0 else 0

    def buildGraph(self):
        """Build the recommendation graph based on video tag similarities."""
        for i in range(len(self.videos)):
            video1 = self.videos[i]
            self.recommendation_graph[video1['title']] = {}
            for j in range(len(self.videos)):
                if i != j:
                    video2 = self.videos[j]
                    # Calculate the weight (similarity) between the videos
                    weight = self.findWeight(video1['tags'], video2['tags'])
                    self.recommendation_graph[video1['title']][video2['title']] = weight

    def getRecommendations(self, video_title):
        """Return the recommendations for a given video title."""
        if video_title in self.recommendation_graph:
            return self.recommendation_graph[video_title]
        else:
            return None

    def displayRecommendations(self):
        """Display all recommendations in a readable format."""
        for video_title, similar_videos in self.recommendation_graph.items():
            print(f"Recommendations for {video_title}:")
            for other_video, weight in similar_videos.items():
                print(f"  - {other_video} with weight: {weight:.2f}")
            print()

# # Step 1: Define the Video Data (title and tags)
# videos = [
#     {'title': 'Video 1', 'tags': {'python', 'tutorial', 'programming'}},
#     {'title': 'Video 2', 'tags': {'python', 'tutorial', 'data science'}},
#     {'title': 'Video 3', 'tags': {'javascript', 'programming', 'web development'}},
#     {'title': 'Video 4', 'tags': {'python', 'tutorial', 'machine learning'}}
# ]

# # Step 2: Create the VideoRecommendationGraph object
# graph = VideoRecommendationGraph(videos)

# # Step 3: Build the recommendation graph based on video similarities
# graph.buildGraph()

# # Step 4: Display all recommendations
# graph.displayRecommendations()

# # Step 5: Get recommendations for a specific video (optional)
# video_title = 'Video 1'
# recommendations = graph.getRecommendations(video_title)
# if recommendations:
#     print(f"\nRecommendations for {video_title}:")
#     for other_video, weight in recommendations.items():
#         print(f"  - {other_video} with weight: {weight:.2f}")