"""
使用T-SNE可视化散点
"""
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE, LocallyLinearEmbedding, Isomap, MDS, SpectralEmbedding


def show_embedding(data, method='tsne', color=None, plot3d=False, **kwargs):
    """
    Scatter plot points in a lower-dimensional embedding space.

    Parameters
    ----------
    data: np.ndarray
        n_samples x n_dimensions
    method: {'tsne', 'locallylinearembedding', 'isomap', 'mds', 'spectralembedding'}

    color: np.ndarray

    plot3d: bool
        whether to embeb in 2d-space or 3d-space
    **kwargs
        other keyword parameters to pass to the model

    SeeAlso
    -------
    sklearn.manifold
    """
    fig = plt.figure()
    if plot3d:
        from mpl_toolkits.mplot3d import Axes3D
        ax = fig.add_subplot(111, projection='3d')
        n_components = 3
    else:
        ax = fig.add_subplot(111)
        n_components = 2
    models = {
        'tsne': TSNE,
        'locallylinearembedding': LocallyLinearEmbedding,
        'isomap': Isomap,
        'mds': MDS,
        'spectralembedding': SpectralEmbedding
    }
    model = models[method.lower()](n_components=n_components, **kwargs)
    transformed = model.fit_transform(data)
    ax.scatter(*transformed.tolist(), c=color)
