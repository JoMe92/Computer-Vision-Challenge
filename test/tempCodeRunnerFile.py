# display the image patches
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(1, 1, 1)
# for i, patch in enumerate(cabel_patches):
#     ax = fig.add_subplot(3, len(cabel_patches), len(cabel_patches)*1 + i + 1)
#     ax.imshow(patch, cmap=plt.cm.gray,
#               vmin=0, vmax=255)
#     ax.set_xlabel('cable %d' % (i + 1))

# for i, patch in enumerate(back_patches):
#     ax = fig.add_subplot(3, len(back_patches), len(back_patches)*2 + i + 1)
#     ax.imshow(patch, cmap=plt.cm.gray,
#               vmin=0, vmax=255)
#     ax.set_xlabel('backround %d' % (i + 1))



# # display the patches and plot
# fig.suptitle('Grey level co-occurrence matrix features', fontsize=14, y=1.05)
# plt.tight_layout()
# plt.show()