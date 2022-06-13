import os
import pandas as pd

class ArticleManager:
    """
    This class is saving a new flight to Excel file.
    """
    DATA_PATH = "articles_data/articles.xlsx"
    DATA_COLUMNS = ['link', 'article']

    def read_article_table(self):
        if os.path.exists(ArticleManager.DATA_PATH):
            df = pd.read_excel(ArticleManager.DATA_PATH)
        else:
            df = pd.DataFrame(columns=ArticleManager.DATA_COLUMNS)
        return df.values.tolist()

    def save_article_table(self, data):
        df = pd.DataFrame(data, columns=ArticleManager.DATA_COLUMNS)
        df.to_excel(ArticleManager.DATA_PATH, index=False)

    def update_articles_table(self, articles):
        data = self.read_article_table()

        all_article_links = [a[0] for a in data]
        new_articles = []
        for article in articles:
            if article[0] not in all_article_links:
                new_articles.append(article)

        data += new_articles

        self.save_article_table(data)

    def get_articles_count(self):
        data = self.read_article_table()
        return len(data)

    def search_article_by_keyword(self, keyword):
        data = self.read_article_table()

        results = []
        for article in data:
            if keyword in article[1]:
                results.append(article)

        return pd.DataFrame(results, columns=ArticleManager.DATA_COLUMNS)
