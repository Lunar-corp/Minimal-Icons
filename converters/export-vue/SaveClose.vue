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
    <path d="m21,11v8c0,1.1-.9,2-2,2H5c-1.1,0-2-.9-2-2V5c0-1.1.9-2,2-2h8" /><polyline points="17 21 17 13 7 13 7 21" /><polyline points="7 3 7 8 13 8" /><path d="m17,3l3,3-3,3" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>