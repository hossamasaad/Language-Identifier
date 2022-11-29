import seaborn as sns
import matplotlib.pyplot as plt

class Visualizer:

    def __init__(self, data) -> None:
        self.data = data

    def show_langauges_counts(self, save_fig = False):
        plt.figure(figsize=(20,14))

        total= float(len(self.data['Language']))
        ax= sns.countplot(x= 'Language', data= self.data, order= self.data['Language'].value_counts().index, palette= 'magma')

        for p in ax.patches:
            percentage= '{:.2f}%'.format(100 * p.get_height()/total)
            x= p.get_x() + p.get_width() - 0.75
            y= 1.015 * p.get_height()
            ax.annotate(percentage, (x, y), fontsize=16)
            
        plt.title('Counts and Percentages of Languages', fontsize=24)
        plt.xlabel("Language",fontsize=20)
        plt.ylabel("Count", fontsize=20)
        plt.xticks(size= 18, rotation=90) 
        if save_fig:
            plt.savefig('/home/hossamasaad/Desktop/Workspace/Language Identifier/reports/figures/langauges_count.png')
        
        plt.show()
    
    def show_percentage(self, save_fig=False):

        plt.figure(figsize=(10,10))
        language= self.data['Language'].value_counts().reset_index()
        
        plt.pie(language['Language'],
                labels = language['index'],
                autopct='%.1f%%',
                textprops={'fontsize': 14})
            
        if save_fig:
            plt.savefig("/home/hossamasaad/Desktop/Workspace/Language Identifier/reports/figures/lanuages_pie.png")
        plt.show()