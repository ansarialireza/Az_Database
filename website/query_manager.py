from blog.models import Post
from services.models import Services

class SearchQueryManager:
    @staticmethod
    def search_posts(query):
        """
        Searches for posts where the title or content matches the query string using raw SQL.
        """
        sql_query = """
            SELECT *
            FROM blog_post
            WHERE status = 1 AND (title LIKE %s OR content LIKE %s)
            ORDER BY published_date DESC
        """
        params = [f'%{query}%', f'%{query}%']

        return list(Post.objects.raw(sql_query, params))

    @staticmethod
    def search_services(query):
        """
        Searches for services where the title or content matches the query string using raw SQL.
        """
        sql_query = """
            SELECT *
            FROM services_services
            WHERE status = 1 AND (title LIKE %s OR content LIKE %s)
            ORDER BY published_date DESC
        """
        params = [f'%{query}%', f'%{query}%']

        return list(Services.objects.raw(sql_query, params))

    @staticmethod
    def get_all_posts_and_services():
        """
        Retrieves all posts and services with status=1 without using ORM.
        """
        sql_query_posts = """
            SELECT *
            FROM blog_post
            WHERE status = 1
            ORDER BY published_date DESC
        """
        sql_query_services = """
            SELECT *
            FROM services_services
            WHERE status = 1
            ORDER BY published_date DESC
        """

        posts = list(Post.objects.raw(sql_query_posts))
        services = list(Services.objects.raw(sql_query_services))

        return posts, services
