<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="m9,3h6c3.31,0,6,2.69,6,6v10c0,1.1-.9,2-2,2H5c-1.1,0-2-.9-2-2v-10c0-3.31,2.69-6,6-6Z" /><line x1="3" y1="11" x2="21" y2="11" /><rect x="10" y="11" width="4" height="4" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>