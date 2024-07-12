from .models import Post, Comment
from django.utils import timezone

class PostQueryManager:
    @staticmethod
    def get_all_posts():
        """
        Retrieves all published posts that are currently active.
        """
        current_time = timezone.now()
        query = """
            SELECT * FROM blog_post
            WHERE status = TRUE AND published_date <= %s
            ORDER BY published_date DESC
        """
        return Post.objects.raw(query, [current_time])

    @staticmethod
    def get_posts_by_category(cat_name):
        """
        Retrieves all posts in a specific category that are currently active.
        """
        current_time = timezone.now()
        query = """
            SELECT p.* FROM blog_post p
            INNER JOIN blog_category c ON p.category_id = c.id
            WHERE p.status = TRUE AND p.published_date <= %s AND c.name = %s
            ORDER BY p.published_date DESC
        """
        return Post.objects.raw(query, [current_time, cat_name])

    @staticmethod
    def get_posts_by_author(username):
        """
        Retrieves all posts by a specific author that are currently active.
        """
        current_time = timezone.now()
        query = """
            SELECT p.* FROM blog_post p
            INNER JOIN auth_user u ON p.author_id = u.id
            WHERE p.status = TRUE AND p.published_date <= %s AND u.username = %s
            ORDER BY p.published_date DESC
        """
        return Post.objects.raw(query, [current_time, username])

    @staticmethod
    def get_posts_by_tag(tag_name):
        """
        Retrieves all posts tagged with a specific tag that are currently active.
        """
        current_time = timezone.now()
        query = """
            SELECT p.* FROM blog_post p
            INNER JOIN blog_post_tags pt ON p.id = pt.post_id
            INNER JOIN blog_tag t ON pt.tag_id = t.id
            WHERE p.status = TRUE AND p.published_date <= %s AND t.name = %s
            ORDER BY p.published_date DESC
        """
        return Post.objects.raw(query, [current_time, tag_name])

    @staticmethod
    def search_posts(query):
        """
        Searches for posts where the title or content matches the query string.
        """
        sql_query = """
            SELECT * FROM blog_post
            WHERE status = TRUE AND (title LIKE %s OR content LIKE %s)
        """
        return Post.objects.raw(sql_query, [f'%{query}%', f'%{query}%'])


class CommentQueryManager:
    @staticmethod
    def get_comments_for_post(post):
        """
        Retrieves all approved comments for a specific post.
        """
        query = """
            SELECT * FROM blog_comment
            WHERE post_id = %s AND approved = TRUE
            ORDER BY created_date DESC
        """
        return Comment.objects.raw(query, [post.id])
